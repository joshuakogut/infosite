#!/usr/bin/env python3
"""Sync storefront info from BigCommerce into the local product tables.

Iterates every product on the BigCommerce store, matches its SKU to
Tbproduct.productid, and syncs:

- WebAddress: the product's storefront URL (visible products only).

- tbproductprice Price: the product's normal price into the product's
  base ("*") price row. If that row's PriceType is anything besides P,
  the type is first reset to P (P = static price; C%/M%/S% compute the
  price from cost + margin, which the storefront price would corrupt).

Dry-run by default. Use --apply to write:
    python bigcommerce_sync_info.py          # report only
    python bigcommerce_sync_info.py --apply  # assign WebAddress + Price
"""
import os
import sys
from decimal import Decimal

import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import requests  # noqa: E402

from product.models import Tbproduct, Tbproductprice  # noqa: E402

CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""
STORE_HASH = ""
BASE_URL = f"https://api.bigcommerce.com/stores/{STORE_HASH}/v3"

HEADERS = {
    "X-Auth-Token": ACCESS_TOKEN,
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_store_url():
    """Base storefront URL, e.g. https://www.lceperformance.com."""
    r = requests.get(
        f"https://api.bigcommerce.com/stores/{STORE_HASH}/v2/store",
        headers=HEADERS,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["secure_url"].rstrip("/")


def get_all_products():
    """Yield every BigCommerce product (id, sku, price, url, visibility)."""
    page = 1
    limit = 250
    while True:
        r = requests.get(
            f"{BASE_URL}/catalog/products",
            headers=HEADERS,
            params={
                "page": page,
                "limit": limit,
                "include_fields": "id,name,sku,price,custom_url,is_visible",
            },
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        yield from data.get("data", [])
        meta = data.get("meta", {}).get("pagination", {})
        print(f"Fetched page {page} of {meta.get('total_pages', '?')}")
        if page >= meta.get("total_pages", page):
            break
        page += 1


def main(apply=False):
    base_url = get_store_url()
    print(f"Store: {base_url}")

    visible, hidden, no_local, skipped = 0, 0, [], 0
    url_updates, price_updates, type_resets = [], [], []

    for p in get_all_products():
        sku = (p.get("sku") or "").strip()
        if not p.get("is_visible"):
            hidden += 1
            continue
        visible += 1
        if not sku or not Tbproduct.objects.filter(productid=sku).exists():
            no_local.append((p["id"], p.get("name"), sku))
            continue
        url = base_url + p.get("custom_url", {}).get("url", "")
        current = (
            Tbproduct.objects.filter(productid=sku)
            .values_list("webaddress", flat=True)
            .first()
        )
        if current != url:
            url_updates.append((sku, url))
        else:
            skipped += 1

        # Normal price -> base ("*") price row. A non-P PriceType computes
        # Price from cost + margin, so it must be reset to P first.
        price = p.get("price")
        if price is None:
            continue
        row = (
            Tbproductprice.objects.filter(
                product__productid=sku, pricecode="*"
            )
            .values("guidproductprice", "pricetype", "price")
            .first()
        )
        if row is None:
            print(f"  {sku}: no '*' price row, skipping price")
            continue
        new_price = Decimal(str(price))
        if (row["price"] or 0) != new_price or row["pricetype"] != "P":
            price_updates.append(
                (sku, row["guidproductprice"], row["pricetype"], new_price)
            )
            if row["pricetype"] != "P":
                type_resets.append(sku)

    print(f"\nVisible: {visible}  Hidden: {hidden}")
    print(f"SKUs with no local Tbproduct: {len(no_local)}")
    for bc_id, name, sku in no_local[:20]:
        print(f"  BC {bc_id} name={name!r} sku={sku!r}")
    print(f"URLs already correct: {skipped}  URL updates: {len(url_updates)}")
    print(
        f"Price updates: {len(price_updates)} "
        f"(PriceType reset to P: {len(type_resets)})"
    )

    if not apply:
        print("\nDry run -- nothing written. Re-run with --apply.")
        for sku, url in url_updates[:5]:
            print(f"  {sku} url -> {url}")
        for sku, _, old_type, new_price in price_updates[:5]:
            print(f"  {sku} price ({old_type} -> P) -> {new_price}")
        return

    for sku, url in url_updates:
        Tbproduct.objects.filter(productid=sku).update(webaddress=url)
    for sku, guid, old_type, new_price in price_updates:
        Tbproductprice.objects.filter(guidproductprice=guid).update(
            price=new_price, pricetype="P"
        )
    print(
        f"\nUpdated {len(url_updates)} WebAddress and "
        f"{len(price_updates)} Price values "
        f"({len(type_resets)} PriceType resets)."
    )


if __name__ == "__main__":
    main(apply="--apply" in sys.argv)

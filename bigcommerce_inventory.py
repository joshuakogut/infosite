#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import requests
from sync.models import Productwarehousesummary
from django.db.models import Sum

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


def get_all_products_with_modifiers():
    products_with_modifiers = []
    page = 1
    limit = 5  # You can increase up to 250

    while True:
        print(f"Getting page {page}")
        url = f"{BASE_URL}/catalog/products?include=modifiers&page={page}&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        for product in data.get("data", []):
            if product["is_visible"] and product.get("modifiers"):
                products_with_modifiers.append(
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "sku": product.get("sku", ""),
                    }
                )

        meta = data.get("meta", {}).get("pagination", {})
        if meta.get("current_page") >= meta.get("total_pages", 0):
            break
        if page > limit:
            print("Reached the limit of pages to fetch.")
            break
        page += 1

    return products_with_modifiers


def get_all_products_without_modifiers():
    products_without_modifiers = []
    page = 1
    limit = 250  # You can increase up to 250

    while True:
        print(f"Getting page {page}")
        url = f"{BASE_URL}/catalog/products?include=modifiers&page={page}&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        for product in data.get("data", []):
            if product["is_visible"] and not product.get("modifiers"):
                products_without_modifiers.append(
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "sku": product.get("sku", ""),
                    }
                )

        meta = data.get("meta", {}).get("pagination", {})
        if meta.get("current_page") >= meta.get("total_pages", 0):
            break
        if page > limit:
            print("Reached the limit of pages to fetch.")
            break
        page += 1

    return products_without_modifiers


# === Run it ===
products = get_all_products_without_modifiers()
print(f"Found {len(products)} products without customizations/modifiers:\n")

for p in products:
    # print(f"{p['id']}: {p['name']} (SKU: {p['sku']})")

    # Get the summed qtyavailable for all rows in the queryset
    total_qty = Productwarehousesummary.objects.filter(productid=p["sku"]).aggregate(
        total_available=Sum("available")
    )["total_available"]

    if total_qty is not None:
        total_qty = int(total_qty)  # Convert string to integer
        # print(f"\tTotal available in local DB: {total_qty}")

        # Update the product inventory level in BigCommerce
        update_url = f"{BASE_URL}/catalog/products/{p['id']}"
        inventory_tracking = "product" if total_qty > 0 else "none"
        payload = {
            "inventory_level": (
                0 if total_qty < 0 else total_qty
            ),  # BigCommerce does not allow negative inventory levels
            "inventory_tracking": inventory_tracking,
        }

        response = requests.put(update_url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            print(
                f"SUCCESS update product {p['id']} with inventory level {total_qty} and tracking {inventory_tracking}."
            )
        else:
            print(
                f"FAIL    update product {p['id']}. Status code: {response.status_code}, Response: {response.text}"
            )
    else:
        print("\tNo matching rows found in local DB.")

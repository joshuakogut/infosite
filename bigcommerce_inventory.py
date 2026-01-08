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
    limit = 50

    while True:
        print(f"Getting page {page} for products with modifiers")
        url = f"{BASE_URL}/catalog/products?include=inventory&page={page}&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        for product in data.get("data", []):
            if product.get("modifiers"):
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
        if page > 5:
            break

        page += 1

    return products_with_modifiers


def get_all_products_with_inventory():
    products_with_inventory = []
    page = 1
    limit = 50

    while True:
        print(f"Getting page {page} for products with inventory")
        url = f"{BASE_URL}/catalog/variants?page={page}&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        for variant in data.get("data", []):
            products_with_inventory.append(
                {
                    "id": variant["id"],
                    "product_id": variant["product_id"],
                    "sku": variant.get("sku", ""),
                    "inventory": variant.get("inventory_level", 0),
                }
            )

        meta = data.get("meta", {}).get("pagination", {})
        if meta.get("current_page") >= meta.get("total_pages", 0):
            break
        if page > 5:
            break
        page += 1

    return products_with_inventory


# === Run it ===
print("Fetching products with inventory...")
products = get_all_products_with_inventory()
print(f"Found {len(products)} products with inventory:\n")

for p in products:
    print(
        f"Variant ID: {p['id']}, Product ID: {p['product_id']} (SKU: {p['sku']}, Inventory: {p['inventory']})"
    )

    # Get the summed qtyavailable for all rows in the queryset
    total_qty = Productwarehousesummary.objects.filter(productid=p["sku"]).aggregate(
        total_available=Sum("available")
    )["total_available"]

    if total_qty is not None:
        print(f"Total available in local DB: {total_qty}")
    else:
        print("No matching rows found in local DB.")

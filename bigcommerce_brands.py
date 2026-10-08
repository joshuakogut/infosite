#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import requests

CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""
STORE_HASH = ""
BASE_URL = f"https://api.bigcommerce.com/stores/{STORE_HASH}/v3/catalog/brands"

import csv

OUTPUT_FILE = "brands.csv"

HEADERS = {
    "X-Auth-Token": ACCESS_TOKEN,
    "Accept": "application/json",
}


# ============================================================
# GET ALL BRANDS
# ============================================================


def get_all_brands():
    brands = []
    page = 1
    limit = 250

    while True:
        params = {
            "page": page,
            "limit": limit,
            "include_fields": "name",
        }

        print(f"Fetching page {page}...")

        response = requests.get(
            BASE_URL,
            headers=HEADERS,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        result = response.json()

        page_brands = result.get("data", [])
        brands.extend(page_brands)

        pagination = result.get("meta", {}).get("pagination", {})

        total_pages = pagination.get("total_pages", page)

        print(f"  Got {len(page_brands)} brands " f"(page {page} of {total_pages})")

        if page >= total_pages:
            break

        page += 1

    return brands


# ============================================================
# WRITE CSV
# ============================================================


def write_csv(brands):
    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(
            [
                "Brand",
                "Brand ID",
            ]
        )

        for brand in brands:
            writer.writerow(
                [
                    brand["name"],
                    brand["id"],
                ]
            )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("Getting BigCommerce brands...")

    brands = get_all_brands()

    print(f"\nFound {len(brands)} brands.")

    write_csv(brands)

    print(f"Saved to: {OUTPUT_FILE}")

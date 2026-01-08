#!/usr/bin/env python3
"""
This will guide you to find a spreadsheet and update vendor prices in bulk
"""

import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from portal import Logger

logger = Logger("sync.vendor_price_updater")

from portal.dev_settings import *
from product.models import *
from django.db.models import Q, Count

import uuid
import pandas as pd
import requests
import uuid

if __name__ == "__main__":

    logger.info("Go to \\\\archie\\share\\price_updates and put a sheet in")
    input("Press Enter when done...")

    files = os.listdir("/mnt/share/price_updates")
    price_files = [f for f in files if f.endswith((".xlsx", ".xls", ".csv"))]

    if not price_files:
        logger.error("No price update files found!")
        sys.exit(1)

    logger.info("Found price update files", count=len(price_files))

    # Display the list of price files for the user to choose from
    print("\nAvailable price files:")
    for idx, file in enumerate(price_files, start=1):
        print(f"{chr(64 + idx)}: {file}")

    # Prompt the user to select a file
    while True:
        choice = input("\nSelect a file by letter (A-Z): ").upper()
        if choice.isalpha() and 1 <= ord(choice) - 64 <= len(price_files):
            selected_file = price_files[ord(choice) - 65]
            break
        else:
            print("Invalid choice. Please select a valid letter.")

    logger.info(f"Selected file: {selected_file}")

    # Determine the file type and read the data into a DataFrame
    file_path = f"/mnt/share/price_updates/{selected_file}"
    if selected_file.endswith((".xlsx", ".xls")):
        data = pd.read_excel(file_path)
    elif selected_file.endswith(".csv"):
        data = pd.read_csv(file_path)
    else:
        logger.error("Unsupported file format!")
        sys.exit(1)

    # Display the columns to the user
    print("\nColumns in the selected file:")
    for idx, column in enumerate(data.columns, start=1):
        print(f"{idx}: {column}")

    # Prompt the user to select the column for vendor part ID
    while True:
        try:
            vendor_part_id_col = (
                int(input("\nSelect the column number for Vendor Part ID: ")) - 1
            )
            if 0 <= vendor_part_id_col < len(data.columns):
                vendor_part_id_col_name = data.columns[vendor_part_id_col]
                break
            else:
                print("Invalid column number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Prompt the user to select the column for new price
    while True:
        try:
            new_price_col = int(input("Select the column number for New Price: ")) - 1
            if 0 <= new_price_col < len(data.columns):
                new_price_col_name = data.columns[new_price_col]
                break
            else:
                print("Invalid column number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    logger.info(
        f"Vendor Part ID column: {vendor_part_id_col_name}, New Price column: {new_price_col_name}"
    )

    # Prompt the user to search for a vendor
    search_keyword = input("\nEnter a keyword to search for the vendor: ").strip()

    # Query the Django dataset for matching vendors
    matching_vendors = Tbvendor.objects.filter(name__icontains=search_keyword)

    if not matching_vendors.exists():
        print("No vendors found matching the keyword. Please try again.")
        sys.exit(1)

    # Display the matching vendors
    print("\nMatching vendors:")
    for idx, vendor in enumerate(matching_vendors, start=1):
        print(f"{idx}: {vendor.name}")

    # Prompt the user to select a vendor
    while True:
        try:
            vendor_choice = int(input("\nSelect a vendor by number: ")) - 1
            if 0 <= vendor_choice < len(matching_vendors):
                selected_vendor = matching_vendors[vendor_choice]
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    logger.info(f"Selected vendor: {selected_vendor.name}")

    # Iterate through the rows in the selected spreadsheet
    for index, row in data.iterrows():
        vendor_part_id = row[vendor_part_id_col_name]
        new_price = row[new_price_col_name]

        # Search for matching rows in Tbproductsupplier with the selected vendor
        matching_suppliers = Tbproductsupplier.objects.filter(
            vendorproductid=vendor_part_id, vendor=selected_vendor
        )

        if not matching_suppliers.exists():
            # Ignore, we do not sell every product available
            continue

        # Update the price for each matching supplier
        for supplier in matching_suppliers:
            supplier.price = new_price
            supplier.save()
            logger.info(
                f"Updated price for Vendor Part ID {vendor_part_id} to {new_price}"
            )

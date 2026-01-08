#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from portal import Logger

logger = Logger("sync.pricing")
import logging

# loads a csv for pricing updates

from product.models import *
import uuid
import pandas as pd

pricing_dir = "/share/pricing/"

if __name__ == "__main__":

    logger.info("Requesting vendor...")
    hint = input("Enter vendor name: ")

    candidates = Tbvendor.objects.filter(name__icontains=hint)
    if not candidates.count() == 1:
        logger.warning(
            "Found multiple vendors, please clarify.",
            found=[c.name for c in candidates],
        )

    vendor = candidates.first()
    logger.info(f"Vendor found: {vendor.name}")

    # Try to find a pricing file for this vendor
    pricing_files = os.listdir(pricing_dir)
    vendor_files = [f for f in pricing_files if hint.lower() in f.lower()]
    if len(vendor_files) == 1:
        vendor_file = vendor_files[0]
        logger.info(f"Found pricing file: {vendor_file}")
    else:
        logger.warning(
            "Found multiple pricing files, please clean up.",
            dir=pricing_dir,
            found=vendor_files,
        )

    # Load the pricing file
    df = pd.read_csv(pricing_dir + vendor_file)
    logger.info(f"Loaded pricing file: {df.shape}")

    # Get all the column titles
    columns = df.columns
    logger.info(f"Columns: {columns}")

    assignments = {"SKU": "", "Price": ""}

    logger.info("Assigning columns...")
    for key in assignments.keys():
        if key in columns:
            assignments[key] = key
        else:
            hint = input(f"Enter column for {key}: ")
            assignments[key] = hint

    logger.info("Assignments: ", assignments)
##
## Later: finish out
##

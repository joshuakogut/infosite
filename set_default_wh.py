#!/usr/bin/env python3
"""
This iterates through every kit with a null warehouse and copies one from another kit
"""

import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from portal import Logger

logger = Logger("sync.set_default_wh")

from portal.dev_settings import *
from product.models import *
from django.db.models import Q, Count

import uuid
import pandas as pd
import requests
import uuid

wh_main_guid = "207E1596-4059-4E26-9A02-B4F7E3EB591F"
wh_main = Tbwarehouse.objects.get(guidwarehouse=wh_main_guid)

if __name__ == "__main__":
    kits = (
        Tbproduct.objects.filter(Q(maintaininventorytype=0))
        .annotate(warehouse_count=Count("warehouses"))
        .filter(
            warehouse_count=0, productid__gt=100000
        )  # Added productid > 100000 condition
        # .filter(productid=1016083)
        .order_by("productid")
    )

    logger.info("found kits with no warehouse links", count=kits.count())

    for kit in kits:
        logger.info("checking on", productid=kit.productid, z=kit.description)

        # make a productwarehouse entry for the main warehouse

        wh = Tbproductwarehouse(
            guidproductwarehouse=uuid.uuid4(),
            warehouse=wh_main,
            product=kit,
            reorderincludeinpo=0,
            qtyreserved=0,
            buildchecked=0,
            deleted=0,
        )
        wh.save()

        input("next?")

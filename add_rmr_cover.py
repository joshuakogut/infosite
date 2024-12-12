#!/usr/bin/env python3
"""
This iterates through every slide assembly and ensures that a component for the RMR-COVER is included in the bill of materials
"""

import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from portal import Logger

logger = Logger("sync.add_rmr_cover")

from portal.dev_settings import *
from product.models import *
from django.db.models import Q
from shipstation.api import *

import uuid
import pandas as pd
import requests
import uuid

rmrcover_guid = "602BFA2E-AEBA-4037-AC04-C7A9C2475B4C"
wh_guid = "7088FE09-EF7F-4596-95B6-262406C1A1F5"

if __name__ == "__main__":
    slides = Tbproduct.objects.filter(
        Q(productid__startswith="gss"), status=1, discontinued=0
    ).order_by("productid")
    logger.info("found slides", count=slides.count())

    for slide in slides:
        logger.info("checking on", productid=slide.productid)

        # search for an existing matching component
        if slide.components.filter(componentguidproduct=rmrcover_guid).count() == 0:
            logger.info("has no component, adding it")
            comp = Tbproductcomponent(
                guidproductcomponent=uuid.uuid4(),
                product=slide,
                componenttype="P",
                note="auto-added",
                componentguidproduct=rmrcover_guid,
                guidcomponentwarehouse=wh_guid,
                quantity=1,
                variablequantity=False,
                cost=0,
                sequence=None,
            )
            comp.save()
        else:
            logger.warning("already has component")

        input("next?")

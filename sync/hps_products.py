#!/usr/bin/env python3

import os, sys, time, glob, csv
import django
import zipfile
import shutil
from decimal import Decimal
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()


from portal import Logger

logger = Logger("sync.host.turn14")

from product.models import *
from sync.models import TmpHpsPrices

import pandas as pd
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

if __name__ == "__main__":
    try:

        logger.info("Finding Launch products")
        launch_ps = (
            Tbproductsupplier.objects.filter(
                Q(vendor__name="Launch Distribution")
                | Q(vendor__name="HPS Performance Products")
            )
            # .filter(product__availonweb=True)
            .exclude(product__productid__iendswith="-old").exclude(
                product__productid="9560002"
            )
        )
        products = []
        for ps in launch_ps:
            products.append(ps.product)
            """logger.info(
                "Found candidate",
                productid=ps.product.productid,
                vendorproductid=ps.vendorproductid,
            )"""

        for product in products:
            # logger.info("Processing product", productid=product.productid)
            # check that the product suppliers has an HPS entry
            if (
                product.suppliers.filter(
                    vendor__name="HPS Performance Products"
                ).count()
                == 0
            ):
                logger.warning(
                    "No HPS supplier entry found. Making one from the launch entry",
                    productid=product.productid,
                )
                ps = product.suppliers.get(vendor__name="Launch Distribution")
                hps_ps = Tbproductsupplier(
                    guidproductsupplier=uuid.uuid4(),
                    vendor=Tbvendor.objects.get(name="HPS Performance Products"),
                    vendorproductid=ps.vendorproductid,
                    product=product,
                    preferred=True,
                )
                hps_ps.save()
            else:
                logger.info("HPS supplier entry found", productid=product.productid)

            try:
                # un-prefer the launch product
                lps = product.suppliers.get(vendor__name="Launch Distribution")
                lps.preferred = False
                lps.save()
            except ObjectDoesNotExist:
                logger.warning(
                    "No launch supplier entry found to demote",
                    productid=product.productid,
                )

            # update the product purchase price
            ps = product.suppliers.get(vendor__name="HPS Performance Products")
            query = TmpHpsPrices.objects.filter(sku=ps.vendorproductid)
            if query.count() > 0:
                HPS = query.first()
                newcost = HPS.msrp * Decimal(0.65)
                logger.info(
                    "Updating purchase price",
                    productid=product.productid,
                    old=ps.vendorprice,
                    new=newcost,
                )
                ps.vendorprice = newcost
                ps.unit = "Ea"
                ps.save()

                try:
                    # update the list price
                    price = product.prices.get(pricetype="P")
                    logger.info(
                        "Update list price",
                        productid=product.productid,
                        old=price.price,
                        new=HPS.map,
                    )
                    price.price = HPS.map
                    price.save()

                except ObjectDoesNotExist:
                    logger.warning(
                        "No static list price found. Skipping update",
                        productid=product.productid,
                    )

            else:
                logger.error(
                    "No HPS price entry found. Skipping update",
                    productid=product.productid,
                    vendor=ps.vendorproductid,
                )

    except Exception as e:
        logger.error(f"An error occurred: {e}")

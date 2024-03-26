#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import tabulate
from django.utils import timezone
from sync.host import trailgear
from product.models import *

from portal import Logger

logger = Logger("sync.trailgear.stock")

from sync.agent import Agent
import json
from sync.host import volusion
from datetime import datetime, timedelta

MISSING_TG_CACHE = "missing_tg_skus.json"
TIME_THRESHOLD = datetime.now() - timedelta(hours=1)


def write_missing_products(missing_prods):
    if len(missing_prods) > 0:
        with open(MISSING_TG_CACHE, "w") as handle:
            json.dump(missing_prods, handle, indent=4)


def trailgear_products():
    ps = (
        Tbproductsupplier.objects.filter(vendor__name="Trail Gear")
        .filter(preferred=True)
        .exclude(product__discontinued=True)
        .exclude(vendorproductid__isnull=True)
        .filter(lastsync__lt=TIME_THRESHOLD)
        .order_by("lastsync")
    )

    logger.info("productsupplier where vendor = tg", count=ps.count())
    return ps


def discover_products(work):
    inp = input("wanna lookup old ones? y/N> ").lower()
    if inp.startswith("y"):
        driver = Agent(headless=False)
        for ps in work:
            data = trailgear.search_for_product(driver, ps)
            if data:
                ps.set_remote_stock(data.stock)
                ps.save()

                upload_product_info(ps)

            else:
                logger.error(
                    "sync.host.trailgear.search_for_product failed to return anything",
                    id=ps.vendorproductid,
                )


def scrape_products(work):

    driver = Agent(headless=False)

    for ps in work:
        data = trailgear.scrape_product(driver, uri=ps.remoteid)
        if data:
            ps.set_remote_stock(data.stock)
            ps.save()

            upload_product_info(ps)
    logger.info("products still needing scraped", count=work.count())


def upload_product_info(ps):
    product = {
        "ProductCode": ps.product.productid,
        "StockStatus": ps.remotestock,
        "ProductPrice": ps.product.WebPrice,
        "ProductManufacturer": "Trail-Gear",
        "ProductDescription_AbovePricing": "by Trail-Gear",
        "Vendor_PartNo": ps.vendorproductid,
    }
    volusion.update_products([product])


if __name__ == "__main__":

    products = trailgear_products()

    unknown = products.filter(remoteid__isnull=True)
    discover_products(unknown)

    known = products.filter(remoteid__isnull=False)
    scrape_products(known)

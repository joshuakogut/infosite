#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import tabulate
from django.utils import timezone
from sync.host.trailgear import *
from product.models import *

from portal import Logger

logger = Logger("sync.trailgear.stock")

from sync.host.volusion import update_products
from datetime import datetime, timedelta


time_threshold = datetime.now() - timedelta(hours=12)


def write_missing_products(missing_prods):
    if len(missing_prods) > 0:
        with open("missing_tg_skus.json", "w") as handle:
            json.dump(missing_prods, handle, indent=4)


def trailgear_products(limit=10):
    prods = []
    db = (
        Tbproductsupplier.objects.filter(vendor__name="Trail Gear")
        .exclude(product__discontinued=True)
        .exclude(vendorproductid__isnull=True)
        .filter(lastsync__lt=time_threshold)
    )

    for supply in db.order_by("lastsync"):
        if supply.vendorproductid != None and supply.vendorproductid.strip() != "":
            try:
                prods.append(supply)
            except Tbproduct.DoesNotExist:
                pass

    work = prods[:limit]

    driver = Agent(headless=False)

    with open("missing_tg_skus.json", "r") as handle:
        missing_prods = json.load(handle)
        logger.info("loaded missing skus", count=len(missing_prods))

    try:
        stock_payload = []
        for ps in work:
            # print("Scraping %s\t%s" % (ps.product.productid,ps.vendorproductid))
            if ps.vendorproductid.strip().lower() not in [k[2] for k in missing_prods]:
                data = search_sku(driver, ps.vendorproductid)
                if data:
                    ps.set_remote_stock(data.stock)
                    ps.save()

                    product = {
                        "ProductCode": ps.product.productid,
                        "StockStatus": ps.remotestock,
                        "ProductPrice": ps.product.WebPrice,
                        "ProductManufacturer": "Trail-Gear",
                        "ProductDescription_AbovePricing": "by Trail-Gear",
                        "Vendor_PartNo": ps.vendorproductid,
                    }
                    update_products([product])

                else:
                    logger.warning(
                        "Could not find part, adding to missing_skus",
                        product=ps.product.productid,
                        vendorproductid=ps.vendorproductid,
                    )
                    missing_prods.append(
                        (
                            ps.product.productid,
                            ps.product.description,
                            ps.vendorproductid.strip().lower(),
                        )
                    )
                    write_missing_products(missing_prods)
            else:
                logger.info(
                    "Skipped missing sku",
                    productid=ps.product.productid,
                    vendorproductid=ps.vendorproductid,
                )
                ps.lastsync = timezone.now()
                ps.save()

        ps = (
            Tbproductsupplier.objects.filter(vendor__name="Trail Gear")
            .exclude(product__discontinued=True)
            .exclude(vendorproductid__isnull=True)
            .filter(lastsync__lt=time_threshold)
        )

        logger.info("products still needing scraped", count=ps.count())

    finally:

        driver.quit()

        """if len(stock_payload) > 0:
            print("Sending stock for %s products to volusion" % len(stock_payload))
            response = update_stock( stock_payload )
            if response.ok:
                print("Success")
            else:
                print("fail")
                """

        write_missing_products(missing_prods)


if __name__ == "__main__":
    trailgear_products(limit=900)

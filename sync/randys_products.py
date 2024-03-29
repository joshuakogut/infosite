#!/usr/bin/env python3

import os
import sys
import re
import humanfriendly as hf
import os, sys
import django
from django.db.models import Q

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from portal import Logger
from product.models import Tbproductsupplier
from portal.settings import RPP_USER, RPP_PASS
from django.utils import timezone
from sync.agent import Agent
import json

logger = Logger("sync.host.randys")

from sync.host.volusion import update_products

root_url = "https://www.randysworldwide.com/"
producturl = "https://www.randysworldwide.com/shop/%s"
search_url = "https://www.randysworldwide.com/shop/?q=%s"


def rpp_products():
    ps = (
        Tbproductsupplier.objects.filter(vendor__name="Randy's Ring & Pinion")
        .filter(preferred=True)
        .exclude(product__discontinued=True)
        .exclude(vendorproductid__isnull=True)
        .exclude(vendorproductid__contains="LC")
        .order_by("lastsync")
    )

    logger.info("productsupplier where vendor = randys", count=ps.count())

    return ps


def discover_products(products):

    inp = input("wanna lookup old ones? y/N> ").lower()
    if inp.startswith("y"):
        driver = Agent(headless=False)
        try:
            for ps in products:
                logger.debug(
                    "Finding remoteid for",
                    productid=ps.product.productid,
                    sku=ps.vendorproductid,
                )

                driver.get(search_url % ps.vendorproductid)

                sort = driver.find_elements("xpath", '//div[@class="sort__group"]')
                prod = driver.find_elements(
                    "xpath", '//div[@class="card product-rich"]'
                )
                if len(sort) == 1:
                    for p in prod:
                        sku = p.find_elements("xpath", "div[2]/div/span[1]")
                        btn = p.find_elements("xpath", "//a")
                        if len(sku) > 0:
                            if sku[0].text.lower() == ps.vendorproductid.lower():
                                remoteid = p.find_element(
                                    "xpath", "div[2]/div[1]/form/a"
                                ).get_attribute("href")
                                ps.remoteid = remoteid
                                ps.save()

                                logger.info(
                                    "found new remoteid",
                                    remoteid=remoteid.split("/").pop(),
                                    ps=ps.vendorproductid,
                                    id=ps.product.productid,
                                )

                else:
                    logger("I don't know what happened", sku=ps.vendorproductid)

        finally:
            driver.quit()


def scrape_products(products):
    driver = Agent(headless=False)

    for ps in products:

        driver.get(ps.remoteid)

        sort = driver.find_elements("xpath", '//div[@class="sort__group"]')
        prod = driver.find_elements("xpath", '//div[@class="prod_wrapper"]')
        if len(sort) == 1:
            # listing page, not an exact match
            logger.error(
                "invalid remote id",
                sku=ps.vendorproductid,
                productid=ps.product.productid,
                remoteid=ps.remoteid,
            )
            ps.remoteid = None
            ps.save()
        elif len(prod) == 1:
            stock = 0
            stocks = driver.find_elements(
                "xpath", '//span[@class="warehouse-availability__stock"]'
            )
            for st in stocks:
                try:
                    stock += int(st.text)
                except:
                    pass

            ps.set_remote_stock(stock)
            ps.save()

            product = {
                "ProductCode": ps.product.productid,
                "StockStatus": ps.remotestock,
                "ProductPrice": ps.product.WebPrice,
                "ProductManufacturer": "Randy's Worldwide",
                "ProductDescription_AbovePricing": "by Randy's Worldwide",
                "Vendor_PartNo": ps.vendorproductid,
            }
            update_products([product])
        else:
            logger("I don't know what happened", sku=ps.vendorproductid)


import datetime

if __name__ == "__main__":

    products = rpp_products()

    unknown = products.filter(remoteid__isnull=True)
    discover_products(unknown)

    known = products.filter(remoteid__isnull=False)
    for ps in known:
        logger.info(a=ps.product.productid, b=ps.remoteid)
    scrape_products(known)

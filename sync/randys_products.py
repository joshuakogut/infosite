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
from portal.models import Tbproductsupplier
from django.utils import timezone
from sync.agent import Agent
import json

logger = Logger("sync.host.randys")

from sync.host.volusion import update_stock

root_url = "https://www.randysworldwide.com/"
producturl = "https://www.randysworldwide.com/shop/%s"
search_url = "https://www.randysworldwide.com/shop/?q=%s"

rpp_username = "***REMOVED***"
rpp_password = "***REMOVED***"


def rpp_products():
    ps = (
        Tbproductsupplier.objects.filter(vendor__name="Randy's Ring & Pinion")
        .exclude(product__discontinued=True)
        .exclude(vendorproductid__isnull=True)
        .exclude(vendorproductid__contains="LC")
        .order_by("lastsync")
    )

    res = ps.count()
    print("results: %s" % res)

    return ps.order_by("lastsync")


def write_missing_products(missing_prods):
    if len(missing_prods) > 0:
        with open("missing_rpp_skus.txt", "w") as handle:
            json.dump(missing_prods, handle)


def triage_products():
    products = rpp_products()

    unknown = products.filter(remoteid__isnull=True)
    known = products.filter(remoteid__isnull=False)

    discover_products(unknown)
    scrape_products(known)


def discover_products(products):

    inp = input("wanna lookup old ones? y/N> ").lower()
    if inp.startswith("y"):
        driver = Agent(headless=False)
        try:
            for ps in products:
                logger.debug(
                    "Finding remoteid for",
                    productid=ps.product.productid,
                    desc=ps.product.description,
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
                                remoteid = (
                                    p.find_element("xpath", "div[2]/div[1]/form/a")
                                    .get_attribute("href")
                                    .split("/")
                                    .pop()
                                )
                                ps.remoteid = remoteid
                                ps.save()

                                logger.info(
                                    "found new remoteid",
                                    remoteid=remoteid,
                                    ps=ps.vendorproductid,
                                    id=ps.product.productid,
                                )

                else:
                    logger("I don't know what happened", sku=ps.vendorproductid)

        finally:
            driver.quit()


def scrape_products(products):
    driver = Agent(headless=False)
    try:

        for ps in products:

            driver.get(producturl % ps.remoteid)

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

                update_stock(
                    [
                        (
                            ps.product.productid,
                            ps.remotestock,
                            "Randy's Worldwide",
                            ps.vendorproductid,
                        )
                    ]
                )
            else:
                logger("I don't know what happened", sku=ps.vendorproductid)

    finally:
        driver.quit()


import datetime

if __name__ == "__main__":
    triage_products()

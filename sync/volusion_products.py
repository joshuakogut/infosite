#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import tabulate
from django.utils import timezone

from sync.models import Volusionproducts, Tbproduct

from sync.host.volusion import get_products, update_products

import re
import requests
import xmltodict

from bs4 import BeautifulSoup

from portal import Logger

logger = Logger("sync.volusion.prods")

PAUSE_ON_ERROR = False


def get_volusion_products():
    for payload in get_products(limit=1499):
        if "ProductPrice" in payload:

            defs = {
                k.lower(): v
                for k, v in payload.items()
                if k.lower() in Volusionproducts.__dict__.keys()
            }
            defs["lastmodified"] = translate_volusion_ts(payload["LastModified"])

            # If we have a matching local product
            if Tbproduct.objects.filter(productid=payload["ProductCode"]).count() > 0:
                acct_product = Tbproduct.objects.get(productid=payload["ProductCode"])
                acct_static_prices = acct_product.prices.filter(pricetype="P")

                if acct_static_prices.count() > 0:
                    localPrice = acct_static_prices.first()
                    volprice = float(payload["ProductPrice"])
                    if localPrice.price and volprice > float(localPrice.price):
                        logger.info(
                            "Raising local price",
                            id=payload["ProductCode"],
                            newprice=payload["ProductPrice"],
                            oldprice=float(localPrice.price),
                        )
                        localPrice.price = payload["ProductPrice"]
                        localPrice.save()

                vp, created = Volusionproducts.objects.update_or_create(
                    product=acct_product, defaults=defs
                )

                logger.info(
                    "set %s" % payload["ProductCode"], lastmodby=payload["LastModBy"]
                )
            else:
                logger.error(
                    "product has no matching entry in acctivate",
                    id=payload["ProductCode"],
                )
                if PAUSE_ON_ERROR:
                    input()


def translate_volusion_ts(source):
    reg = r"(\d{1,2})\/(\d{1,2})\/(\d{4}) (\d{1,2}):(\d{1,2}):(\d{1,2}) (\w{1,2})"
    matches = re.findall(reg, source)
    MM, DD, YYYY, hh, mm, ss, AM_PM = matches[0]

    if AM_PM == "PM":
        hh = int(hh)
        if hh < 12:
            hh += 12

    return "%s-%s-%s %s:%s:%s" % (YYYY, MM, DD, hh, mm, ss)


def rewrite_products(limit=99):
    # Locate the ones we want to rewrite
    rewrite_candidates = Volusionproducts.objects.filter(
        Q(productdescription__icontains="lcengineering.com")
        | Q(productdescription__icontains="EPA")
    )

    logger.info("found rewrite candidates", count=len(rewrite_candidates))

    for sus in rewrite_candidates[:limit]:

        lce = False
        epa = False

        soup = BeautifulSoup(sus.productdescription, features="html.parser")

        def lce_selector(tag):
            return tag.name == "a" and "lcengineering.com" in tag.text.lower()

        def epa_selector(tag):
            return (
                tag.name == "h3"
                and tag.has_attr("class")
                and "pdhead" in tag.get("class")
                and "epa" in tag.text.lower()
            )

        old_link = soup.find(lce_selector)
        if old_link is not None:
            logger.info(
                "removed lcengineering link from",
                productid=sus.productcode,
                link=old_link.attrs["href"],
            )
            old_link.parent.clear()

        epa_warning = soup.find(epa_selector)
        if epa_warning is not None:
            logger.info("removed EPA warning from", productid=sus.productcode)
            epa_warning.clear()

        if old_link is not None or epa_warning is not None:
            sus.productdescription = str(soup)

            # Send new description up to volusion

            logger.info("updating", productid=sus.productcode)

            update_products(
                [
                    {
                        "ProductCode": sus.productcode,
                        "ProductDescription": sus.productdescription,
                    }
                ]
            )
            sus.save()


def identify_underpriced():
    # Find available products
    available = (
        Tbproduct.objects.filter(availonweb=True)
        .filter(status=1)  # must be active
        .filter(discontinued=False)  # Make sure we're buying/producing it
        .exclude(assemblytype="K")  # Ignore kits, that shit is complicated
        .exclude(webproduct__isnull=True)  # need a matching entry reported by volusion
        .order_by("-updateddate")  # most recently updated in acctivate
    )

    bad = 0
    for product in available:
        try:
            current_price = product.webproduct.productprice
            proposed_price = product.WebPrice
            price_difference = proposed_price - current_price

            if price_difference > 0.50:  # Only show price increases over 50 cents
                bad += 1
                PCT_OVER_WEB = (price_difference * 100) / (
                    (current_price + proposed_price) / 2
                )
                PCT_PROFIT = (
                    (proposed_price - product.anycost) * 100
                ) / product.anycost

                pct = PCT_PROFIT
                if pct > 30:
                    logger.info(
                        "%.2f%%" % pct,
                        id=product.productid,
                        desc=product.description.replace("\n", " ")[:30],
                        cost="%.2f" % product.anycost,
                        price_current="%.2f" % current_price,
                        price_proposed="%.2f" % proposed_price,
                        z_type=product.prices.first().pricetype,
                        z_price="%.2f" % product.prices.first().price,
                    )
        except Exception as e:
            logger.error(
                "error processing product", productid=product.productid, error=e
            )

    logger.info("products under expected price", count=bad)


if __name__ == "__main__":

    logger.info("INSTRUCTIONS: Go clear out the product sync history in volusion.")

    get_volusion_products()

    con = input("find out of pocket pricing? y/N")
    if con.lower() == "y":

        # TODO: pull the modification out of here and report how out of pocket stuff is before asking to update
        identify_underpriced()

"""         _               
 _ __  _ __(_) ___ ___  ___ 
| '_ \| '__| |/ __/ _ \/ __|
| |_) | |  | | (_|  __/\__\\
| .__/|_|  |_|\___\___||___/
|_|     

prices = Tbproductprice.objects              \
    .filter(product__availonweb=True)        \
    .filter(product__discontinued=False)     \
    .filter(product__status=True)            \
    .filter(pricetype='P')
    
print( prices.count() )

payload = []
for price in prices[ :100 ]:       
    payload.append((price.product.productid, price.price))

result = update_stock( payload )
if result.ok:
    print("Seems like a success")
else:
    raise Exception( result )

    """

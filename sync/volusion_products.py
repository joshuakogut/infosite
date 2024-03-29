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


def get_volusion_products():
    infos = get_products(limit=699)

    for prod in infos:
        if "ProductPrice" in prod:

            defs = {
                k.lower(): v
                for k, v in prod.items()
                if k.lower() in Volusionproducts.__dict__.keys()
            }
            defs["lastmodified"] = translate_volusion_ts(prod["LastModified"])
            vp, created = Volusionproducts.objects.update_or_create(
                productcode=prod["ProductCode"], defaults=defs
            )
            ap = Tbproduct.objects.get(productid=prod["ProductCode"])
            aprices = ap.prices.filter(pricetype="P")
            if aprices.count() > 0:
                p = aprices.first()
                if prod["ProductPrice"] > p.price:
                    logger.info(
                        "Raising local price",
                        id=prod["ProductCode"],
                        newprice=prod["ProductPrice"],
                        oldprice=p.price,
                    )
                    # p.price = prod['ProductPrice']
                    # p.save()

            print("set %s" % prod["ProductCode"])

    print("recorded %s products" % len(infos))


def translate_volusion_ts(source):
    reg = r"(\d{1,2})\/(\d{1,2})\/(\d{4}) (\d{1,2}):(\d{1,2}):(\d{1,2}) (\w{1,2})"
    matches = re.findall(reg, source)
    MM, DD, YYYY, hh, mm, ss, OS = matches[0]

    if OS == "PM":
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


if __name__ == "__main__":
    # pull the web products
    logger.info("INSTRUCTIONS: Go clear out the product sync history in volusion.")
    # input("continue >")

    get_volusion_products()

    # synchronize available info
    available = (
        Tbproduct.objects.filter(availonweb=True)
        .filter(discontinued=False)
        .order_by("-updateddate")[:100]
    )
    for product in available:
        try:
            vp = Volusionproducts.objects.get(productcode=product.productid)
            logger.info(
                id=product.productid,
                desc=product.description,
                webprice="%.2f" % vp.productprice,
                updateprice="%.2f" % product.WebPrice,
            )
        except Exception as e:
            logger.error(
                "no matching volusion product",
                code=product.productid,
                desc=product.description,
            )


"""        _               
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

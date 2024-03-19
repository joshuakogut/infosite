#!/usr/bin/env python3
import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import tabulate
from django.utils import timezone

from portal.models import *

from sync.host.volusion import product_info

import re
import requests
import xmltodict


def web_products():
    infos = product_info()

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


if __name__ == "__main__":
    # web_products()

    #         _             _
    #     ___| |_ ___   ___| | __
    #    / __| __/ _ \ / __| |/ /
    #    \__ \ || (_) | (__|   <
    #    |___/\__\___/ \___|_|\_\

    available = Productwarehousesummary.objects.filter(product__availonweb=True).filter(
        warehouse
    )


"""
 
            _               
 _ __  _ __(_) ___ ___  ___ 
| '_ \| '__| |/ __/ _ \/ __|
| |_) | |  | | (_|  __/\__ \
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

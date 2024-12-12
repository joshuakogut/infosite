#!/usr/bin/env python3
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

# your imports, e.g. Django models
from sync.models import Volusionproducts
from sync.host.volusion import update_products
from sync.models import VolusionDescriptions
import re


prods = Volusionproducts.objects.filter(productdescription__startswith="h1")

limit = 50
send = []

for p in prods[:limit]:
    fix = VolusionDescriptions.objects.get(productcode=p.product_id)
    p.productdescription = fix.productdescription.replace("search", "replace")
    print("fixed %s" % p.product_id)
    p.save()
    send.append(
        {"ProductCode": p.product_id, "ProductDescription": p.productdescription}
    )

update_products(send)

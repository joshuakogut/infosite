#!/usr/bin/env python3
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

# your imports, e.g. Django models
from portal.models import Volusionproducts

prods = Volusionproducts.objects.filter(productdescription__contains="EPA")
for p in prods:
    desc = p.productdescription.split("\n")
    i = 0
    for line in desc:
        if line.find("EPA") > -1:
            p.productdescription = "\n".join(desc[0:i])
            print("fixed %s" % p.productcode)
            p.save()
            continue
        else:
            i += 1

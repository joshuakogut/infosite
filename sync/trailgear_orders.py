#!/usr/bin/env python3
import os, sys
import django
from django.db.models import Q

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

import tabulate
from django.utils import timezone

from portal import Logger

logger = Logger("sync.trailgear.orders")

import json

from portal.models import *
from sync.host.trailgear import *
import uuid
from tracking_numbers import get_tracking_number


def trailgear_orders(limit=10):
    prods = []
    pos = (
        Tbpo.objects.filter(vendor__name="Trail Gear")
        .filter(order__isnull=False)
        .exclude(postatus="X")
        .filter(Q(supplierstatus=None) | Q(supplierstatus="processing"))
        .order_by("supplierstatus")
        .order_by("-suppliersyncdate")
        .order_by("dateissued")
    )
    # .filter(supplierstatus=None)

    work = pos[:limit]

    flat = [
        [
            po.ponumber,
            po.dateissued,
            po.supplierstatus,
            po.order.ordernumber,
            po.order.customer.name,
        ]
        for po in work
    ]

    return work


if __name__ == "__main__":

    # while True:
    pos = trailgear_orders(limit=50)

    logger.info("Launching agent")
    driver = Agent()

    driver.get(root_url)
    driver.load_cookies()
    driver.get(history_url)
    check_login(driver)

    try:
        with open("missing_rpp_skus.txt", "r") as handle:
            missing_prods = json.load(handle)
            logger.info("loaded missing skus", count=len(missing_prods))

        for po in pos:
            if (
                po.order.shipments.filter(
                    webshipmentid__startswith="trailgear/"
                ).count()
                > 0
            ):
                data = search_order(driver, po.ponumber)
                logger.info("shipment exists, setting status", status=data.status)
                po.supplierstatus = data.status
                po.suppliersyncdate = timezone.now()
                po.save()
            else:

                logger.info("Scraping PO", PO=po.ponumber)

                data = search_order(driver, po.ponumber)
                if data:

                    if len(data.packages) > 0:
                        shipnum = driver.find_element(
                            "xpath", '//div[@class="order-title"]/strong'
                        ).text.split("#")[1]
                        parsed = get_tracking_number(data.packages[0])
                        carrier = "Dealer"
                        try:
                            carrier = parsed.courier.code
                        except:
                            pass

                        if (
                            Tbshipment.objects.filter(shipmentnumber=shipnum).count()
                            == 0
                        ):
                            shipment = Tbshipment(
                                guidshipment=uuid.uuid4(),
                                customer=po.order.customer,
                                readytoprint=True,
                                printed=False,
                                exported856=False,
                                freightcollect=False,
                                insured=False,
                                shipmentnumber=shipnum,
                                shipmentstatus="S",
                                carrier=carrier,
                                createdby="JK",
                                createddate=timezone.now(),
                                webshipmentid="trailgear/%s" % shipnum,
                            )
                        else:
                            shipment = Tbshipment.objects.get(shipmentnumber=shipnum)

                        shipment.updatedby = "JK"
                        shipment.updateddate = timezone.now()
                        shipment.websyncdate = timezone.now()
                        shipment.save()

                        existing = [p.carrierpackageid for p in shipment.packages.all()]
                        for tracker in data.packages:
                            if tracker not in existing:
                                logger.info(
                                    "Added tracking number",
                                    carrier=carrier,
                                    tracking=tracker,
                                )
                                pkg = Tbshipmentpack(
                                    guidshipmentpack=uuid.uuid4(),
                                    shipment=shipment,
                                    voided=False,
                                    notbillable=True,
                                    carrierpackageid=tracker,
                                    comment="from Trail Gear",
                                )
                                pkg.save()

                        if (
                            Tbshipmentorder.objects.filter(
                                shipment=shipment, order=po.order
                            ).count()
                            == 0
                        ):
                            so = Tbshipmentorder(
                                guidshipmentorder=uuid.uuid4(),
                                shipment=shipment,
                                order=po.order,
                            )
                            so.save()

                        logger.info(
                            "Applied tracking numbers to order",
                            count=len(data.packages),
                            order=po.order.ordernumber,
                            po=po.ponumber,
                        )

                    po.supplierstatus = data.status
                    po.suppliersyncdate = timezone.now()
                    logger.info(
                        "po.supplierstatus updated",
                        po=po.ponumber,
                        status=po.supplierstatus,
                    )
                    po.save()
                else:
                    logger.error("No order found")
                    po.suppliersyncdate = timezone.now()
                    po.supplierstatus = "404"
                    po.save()

    finally:
        driver.quit()

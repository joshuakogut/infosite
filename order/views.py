from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
from portal import models
import opaque


def index(request):
    orders = models.PortalOrderList.objects.order_by("-orderdate", "-ordernumber")

    paginator = Paginator(orders, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {"page_obj": page_obj}

    return render(request, "order/list.html", ctx)


def status(request, token):
    encoder = opaque.OpaqueEncoder(2031)
    order_number = encoder.decode_base64(token)

    order = models.Tborders.objects.get(ordernumber=order_number)
    ships = order.shipments.all()
    ctx = {
        "order": order,
        "details": [
            {
                "subline": od.sublinenumber,
                "productid": od.productid,
                "hasimg": od.product.productpicture != None,
                "linetype": od.linetype,
                "description": od.description,
                "qtyordered": od.qtyordered,
                "qtyscheduled": od.qtyscheduled,
                "qtyshipped": od.qtyshipped,
                "allocated": od.qtyscheduled + od.qtyshipped == od.qtyordered,
                "price": od.price,
                "vendor": od.vendor.name if od.createpo == True else False,
                "ordered_on": "",  # ""od.linetype, #od.podetail.po.dateissued if od.createpo==True else False
            }
            for od in order.details.order_by("linenumber", "sublinenumber")
        ],
        "count": order.shipments.count(),
        "packages": [
            {
                "tracking": p.carrierpackageid,
                "date": shp.shipmentdate,
                "carrier": shp.carrier,
                "service": shp.carrierservice,
            }
            for shp in order.shipments.all()
            for p in shp.packages.all()
        ],
    }
    return render(request, "order/status.html", ctx)


""" Auto redirects to any order number """
"""
def redirect(request, order_number):
    encoder = opaque.OpaqueEncoder(2031)
    token = encoder.encode_base64(order_number)
    
    response = HttpResponse(status=302)
    response['Location'] = '/order/%s' % token.decode()
    return response
"""

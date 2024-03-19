from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from portal import models


def index(request):
    # products = models.Tbproduct.objects.filter(status=1,availonweb=1)
    products = models.ProductList.objects.filter(qtyordered__gt=0).order_by("-gross")

    paginator = Paginator(products, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {"page_obj": page_obj}

    return render(request, "product/list.html", ctx)


def image(request, productid):
    product = models.Tbproduct.objects.get(productid=productid)
    return HttpResponse(product.productpicture, content_type="image/jpeg")


def detail(request, productid):
    product = models.Tbproduct.objects.get(productid=productid)
    info = models.Volusionproducts.objects.get(productcode=productid)
    ctx = {"product": product, "info": info}
    return render(request, "product/detail.html", ctx)


def feed(request):
    products = models.PortalProductFeed.objects.all()

    response = HttpResponse(content_type="text/plain")
    response.write("id\tprice\tquantity")
    for product in products:
        qty = product.quantity.normalize()
        if qty < 0:
            qty = 0
        response.write("\n%s\t%s\t%d" % (product.id.strip(), product.price, qty))

    return response

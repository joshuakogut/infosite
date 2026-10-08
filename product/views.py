from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotModified
from django.utils.http import quote_etag
from product.models import Tbproduct
from sync.models import Volusionproducts

# Served for products with no stored picture (4,539 of 9,732). A plain
# light-grey box served from static/ so the list has no external dependency.
NO_IMAGE_PATH = settings.BASE_DIR / "static" / "no-image.png"


def index(request):
    """Paginated browse list of every product: ID and description.

    Replaces the old index, which queried models.ProductList -- that model
    doesn't exist anywhere in the codebase, so the view 500'd.

    Uses .values() rather than full Tbproduct instances -- the TaxInPrice
    column mapping on the model is broken, so selecting full rows raises
    Invalid column name 'TaxInPrice'.
    """
    products = Tbproduct.objects.values("productid", "description").order_by(
        "productid"
    )

    paginator = Paginator(products, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {"page_obj": page_obj}

    return render(request, "product/list.html", ctx)


def _image_content_type(data: bytes) -> str:
    """Detect the image type from magic bytes.

    ProductPicture is untyped varbinary: of the first 300 non-null rows,
    263 were JPEG, 35 GIF and 2 PNG, so the content type must be sniffed
    rather than hardcoded.
    """
    if data[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return "application/octet-stream"


def image(request, productid):
    """Serve the ProductPicture varbinary with a sniffed content type.

    Products with no stored picture (4,539 of 9,732) get a plain grey
    placeholder instead of a 404, so every <img> in the browser list
    resolves. Sends an ETag so the browser can 304 instead of
    re-downloading ~100 images per list page.
    """
    row = (
        Tbproduct.objects.filter(productid=productid)
        .values("productpicture")
        .first()
    )
    if row is None or not row["productpicture"]:
        data = NO_IMAGE_PATH.read_bytes()
        response = HttpResponse(data, content_type="image/png")
        response["Cache-Control"] = "private, max-age=86400"
        return response

    data = bytes(row["productpicture"])
    etag = quote_etag(str(len(data)) + "-" + str(hash(data)))
    if request.META.get("HTTP_IF_NONE_MATCH") == etag:
        return HttpResponseNotModified()

    response = HttpResponse(data, content_type=_image_content_type(data))
    response["ETag"] = etag
    response["Cache-Control"] = "private, max-age=86400"
    return response


def detail(request, productid):
    product = (
        Tbproduct.objects.filter(productid=productid)
        .values("productid", "description")
        .first()
    )
    if product is None:
        return render(request, "product/detail.html", {"product": None}, status=404)
    # Not every product has a web product row (6,718 of 9,732 do), so use
    # first() rather than get() and let the template render without one.
    info = Volusionproducts.objects.filter(product__productid=productid).first()
    ctx = {"product": product, "info": info}
    return render(request, "product/detail.html", ctx)

from django.shortcuts import render
from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.db import connection
from django.http import HttpResponse, HttpResponseNotModified
from django.utils import timezone
from django.utils.http import quote_etag
from datetime import timedelta
from product.models import Tbproduct
from sync.models import Volusionproducts

# Served for products with no stored picture (4,539 of 9,732). A plain
# light-grey box served from static/ so the list has no external dependency.
NO_IMAGE_PATH = settings.BASE_DIR / "static" / "no-image.png"

# Sortable functions for the product browser. Each entry owns its ordering:
# label for the dropdown, the SQL for its window, and whether the "gross"
# revenue column should be shown.
SORTS = {
    "productid": {"label": "Product ID"},
    "gross": {"label": "Gross Revenue"},
}

# Line types that count toward revenue, per the Acctivate resource code list:
# P = product, D = dropship (also a product), S = special order (dropship
# to our office). C (misc charges like Shipping) and N are excluded, as
# are cancelled lines -- those would otherwise let "Shipping" ($812K) and
# "Sales Tax" ($447K) pseudo-products top the ranking.
REVENUE_LINETYPES = ("P", "D", "S")
REVENUE_MONTHS = 12


def index(request):
    """Paginated product browser with sort dropdown.

    Default order is ProductID over every product. Sorting by "gross"
    filters to active PC5 products and orders by 12-month gross revenue
    (SUM of tborderdetail.amount on non-cancelled lines whose LineType is
    P/D/S -- see REVENUE_LINETYPES -- and whose tborders.entrydate is
    within the window).

    Uses .values() rather than full Tbproduct instances -- the TaxInPrice
    column mapping on the model is broken, so selecting full rows raises
    Invalid column name 'TaxInPrice'.

    Gross is computed in raw SQL with a single grouped LEFT JOIN: the ORM
    equivalent is a correlated subquery per product and costs 2.12s for the
    first page vs 0.26s raw, for identical rows.
    """
    sort = request.GET.get("sort", "productid")
    if sort not in SORTS:
        sort = "productid"

    if sort == "gross":
        page_obj = _gross_page(request)
    else:
        rows, _ = _productid_rows()
        paginator = Paginator(rows, 100)
        page_obj = paginator.get_page(request.GET.get("page"))
    ctx = {"page_obj": page_obj, "sort": sort, "sorts": SORTS}

    return render(request, "product/list.html", ctx)


def _productid_rows():
    qs = Tbproduct.objects.values("productid", "description").order_by("productid")
    return qs, qs.count()


def _gross_page(request):
    """One page of (productid, description, gross) dicts, as a page_obj.

    Gross is pre-paged in SQL (OFFSET/FETCH), so this builds the Paginator
    over a same-length placeholder list and swaps in the fetched rows --
    the template's page_obj interface (has_previous/next, number,
    paginator.count/num_pages) works unchanged.
    """
    limit = timezone.now() - timedelta(days=REVENUE_MONTHS * 30)

    base = """
        FROM tbproduct p
        JOIN tbproductclass c ON c.GUIDProductClass = p.GUIDProductClass
        LEFT JOIN (
            SELECT d.GUIDProduct, SUM(d.Amount) AS gross
            FROM tborderdetail d
            JOIN tborders o ON o.GUIDOrder = d.GUIDOrder
            WHERE o.EntryDate >= %s
              AND d.LineCancelled = 0
              AND d.LineType IN ('P', 'D', 'S')
            GROUP BY d.GUIDProduct
        ) g ON g.GUIDProduct = p.GUIDProduct
        WHERE p.Status = 1 AND c.ProductClassID = 'PC5'
    """
    params = [limit]

    with connection.cursor() as cur:
        cur.execute("SELECT COUNT(*) " + base, params)
        total = cur.fetchone()[0]

    per_page = 100
    num_pages = (total + per_page - 1) // per_page or 1
    raw_page = request.GET.get("page") or "1"
    page_number = (
        int(raw_page) if raw_page.isdigit() and int(raw_page) >= 1 else 1
    )
    page_number = min(page_number, num_pages)
    offset = (page_number - 1) * per_page

    with connection.cursor() as cur:
        cur.execute(
            "SELECT p.ProductID, p.Description, ISNULL(g.gross, 0) AS gross "
            + base
            + " ORDER BY gross DESC, p.ProductID "
            + "OFFSET %s ROWS FETCH NEXT 100 ROWS ONLY",
            params + [offset],
        )
        rows = [
            {"productid": r[0], "description": r[1], "gross": r[2]}
            for r in cur.fetchall()
        ]

    paginator = Paginator([None] * total, per_page)
    page_obj = paginator.page(page_number)
    page_obj.object_list = rows
    return page_obj


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

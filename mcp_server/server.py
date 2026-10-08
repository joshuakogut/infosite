"""
MCP server for querying infosite products.

Read-only tools backed by the Acctivate SQL Server database through the
Django ORM models in ``product`` and ``portal``.

Run with stdio (for MCP clients such as Claude Desktop / Cline / VS Code):
    /home/joshua/infosite/.venv/bin/python /home/joshua/infosite/mcp_server/server.py
"""
from __future__ import annotations

import logging
import os
import sys
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

# ---------------------------------------------------------------------------
# Django bootstrap (the server lives in <project>/mcp_server/).
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")

import django  # noqa: E402

django.setup()

# stdout is the JSON-RPC channel for stdio transport; make sure nothing else
# logs to it.
_root = logging.getLogger()
for _h in list(_root.handlers):
    _root.removeHandler(_h)
_root.addHandler(logging.StreamHandler(sys.stderr))
_root.setLevel(logging.WARNING)

from django.db.models import Q  # noqa: E402
from mcp.server.mcpserver import MCPServer  # noqa: E402

from portal.models import Tbwarehouse  # noqa: E402
from product.models import (  # noqa: E402
    Productwarehousesummary,
    Tbproduct,
    Tbproductclass,
    Tbproductprice,
    Tbproductsupplier,
)

MAX_LIMIT = 200


def _clean(value):
    """Make DB values JSON friendly."""
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def _rows(qs) -> list[dict]:
    return [{k: _clean(v) for k, v in row.items()} for row in qs]


def _limit(limit: int) -> int:
    return max(1, min(int(limit), MAX_LIMIT))


server = MCPServer(
    name="infosite-products",
    instructions=(
        "Read-only access to the infosite product database. Start with "
        "search_products to find a product, then use get_product, "
        "get_product_stock, get_product_suppliers and get_product_prices "
        "with the exact productid. Use list_product_classes and "
        "list_warehouses to discover filter values."
    ),
)

PRODUCT_LIST_FIELDS = (
    "productid",
    "description",
    "unit",
    "status",
    "discontinued",
    "producttype",
    "productclass__productclassid",
    "productclass__description",
)


@server.tool(
    name="search_products",
    description=(
        "Search products by product ID or description (case-insensitive "
        "substring; every word in the query must match the ID or description). "
        "Discontinued products are excluded unless include_discontinued=true. "
        "Optionally filter by product class ID (e.g. 'PC5')."
    ),
)
def search_products(
    query: str = "",
    product_class: str = "",
    include_discontinued: bool = False,
    limit: int = 20,
) -> list[dict]:
    qs = Tbproduct.objects.all()
    for word in query.split():
        qs = qs.filter(Q(productid__icontains=word) | Q(description__icontains=word))
    if product_class:
        qs = qs.filter(productclass__productclassid__iexact=product_class)
    if not include_discontinued:
        qs = qs.filter(discontinued=False)
    return _rows(qs.order_by("productid").values(*PRODUCT_LIST_FIELDS)[: _limit(limit)])


@server.tool(
    name="get_product",
    description="Get full details for one product by its exact ProductID.",
)
def get_product(productid: str) -> dict:
    row = (
        Tbproduct.objects.filter(productid__iexact=productid)
        .values(
            "guidproduct", "productid", "description", "altdescription", "unit",
            "status", "discontinued", "producttype", "salescategory",
            "productclass__productclassid", "productclass__description",
            "weight", "length", "width", "height", "volume", "color", "size",
            "leadtime", "specification", "webaddress", "availonweb",
            "notforresale", "innerpackqty", "outerpackqty", "salesunit",
            "purchaseunit", "packageunit", "createddate", "updateddate", "note",
        )
        .first()
    )
    if row is None:
        return {"error": f"Product {productid!r} not found"}
    return {k: _clean(v) for k, v in row.items()}


@server.tool(
    name="get_product_stock",
    description=(
        "Get stock levels per warehouse for a product by exact ProductID: "
        "on hand, booked, available, on PO, reorder point, location and costs."
    ),
)
def get_product_stock(productid: str) -> list[dict]:
    qs = Productwarehousesummary.objects.filter(product__productid__iexact=productid)
    return _rows(
        qs.order_by("warehouse").values(
            "productid", "warehouse", "warehousedescription", "location",
            "qtyonhand", "qtybooked", "qtybackordered", "available",
            "quantityonpo", "quantityonorder", "reorderpoint", "stockinglevel",
            "lastcost", "avgcost", "standardcost", "lasttransactiondate",
            "expectedreceiptdate",
        )
    )


@server.tool(
    name="get_product_suppliers",
    description=(
        "List vendors that supply a product (by exact ProductID) with the "
        "vendor's part number and price."
    ),
)
def get_product_suppliers(productid: str) -> list[dict]:
    qs = Tbproductsupplier.objects.filter(product__productid__iexact=productid)
    return _rows(
        qs.order_by("-preferred", "vendor__name").values(
            "vendor__name", "vendor__vendorid", "vendorproductid", "preferred",
            "vendorprice", "lastprice", "unit", "leadtime", "lastreceiptdate",
        )
    )


@server.tool(
    name="get_product_prices",
    description=(
        "List price records for a product (by exact ProductID): price code, "
        "type, quantity breaks, price and effective dates."
    ),
)
def get_product_prices(productid: str) -> list[dict]:
    qs = Tbproductprice.objects.filter(product__productid__iexact=productid)
    return _rows(
        qs.order_by("pricecode", "lowqty").values(
            "pricecode", "pricetype", "price", "priceunit", "lowqty", "highqty",
            "guidcustomer", "contractid", "effectivedate", "expirationdate",
        )
    )


@server.tool(
    name="search_products_by_vendor_sku",
    description="Find products by the vendor's own part number (substring match).",
)
def search_products_by_vendor_sku(vendor_sku: str, limit: int = 20) -> list[dict]:
    qs = Tbproductsupplier.objects.filter(vendorproductid__icontains=vendor_sku)
    return _rows(
        qs.order_by("vendorproductid").values(
            "product__productid", "product__description", "vendor__name",
            "vendorproductid", "vendorprice", "preferred",
        )[: _limit(limit)]
    )


@server.tool(
    name="list_product_classes",
    description="List product classes (IDs usable as the product_class filter).",
)
def list_product_classes() -> list[dict]:
    return _rows(
        Tbproductclass.objects.order_by("productclassid").values(
            "productclassid", "description", "active"
        )
    )


@server.tool(name="list_warehouses", description="List warehouses.")
def list_warehouses() -> list[dict]:
    return _rows(
        Tbwarehouse.objects.order_by("warehouseid").values(
            "warehouseid", "description", "active"
        )
    )


def main() -> None:
    server.run(transport="stdio")


if __name__ == "__main__":
    main()

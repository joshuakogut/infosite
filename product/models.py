from portal.models import *
from order.models import *
from django.db.models import Q


class Tbproductclass(models.Model):
    guidproductclass = models.CharField(
        db_column="GUIDProductClass", primary_key=True, max_length=36
    )
    itemlistid = models.CharField(
        db_column="ItemListID",
        unique=True,
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    productclassid = models.CharField(
        db_column="ProductClassID",
        unique=True,
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    description = models.CharField(
        db_column="Description",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidsalesaccount = models.CharField(
        db_column="GUIDSalesAccount", max_length=36, blank=True, null=True
    )
    guidreturnsaccount = models.CharField(
        db_column="GUIDReturnsAccount", max_length=36, blank=True, null=True
    )
    guidtradediscountaccount = models.CharField(
        db_column="GUIDTradeDiscountAccount", max_length=36, blank=True, null=True
    )
    guidcgsaccount = models.CharField(
        db_column="GUIDCGSAccount", max_length=36, blank=True, null=True
    )
    active = models.BooleanField(db_column="Active")
    guidcgsadjaccount = models.CharField(
        db_column="GUIDCGSAdjAccount", max_length=36, blank=True, null=True
    )
    guidclass = models.CharField(
        db_column="GUIDClass", max_length=36, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "tbproductclass"


class Tbproduct(models.Model):

    guidproduct = models.CharField(
        db_column="GUIDProduct", primary_key=True, max_length=36
    )
    productclass = models.ForeignKey(
        Tbproductclass,
        on_delete=models.PROTECT,
        db_column="GUIDProductClass",
        related_name="products",
    )
    productid = models.CharField(
        db_column="ProductID",
        unique=True,
        max_length=159,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )

    taxinprice = models.BooleanField(db_column="TaxInPrice")
    allowoverride = models.BooleanField(db_column="AllowOverride")
    allowzero = models.BooleanField(db_column="AllowZero")
    commissiontype = models.SmallIntegerField(
        db_column="CommissionType", blank=True, null=True
    )
    commpct = models.DecimalField(
        db_column="CommPct", max_digits=19, decimal_places=7, blank=True, null=True
    )
    commamt = models.DecimalField(
        db_column="CommAmt", max_digits=19, decimal_places=4, blank=True, null=True
    )
    unit = models.CharField(
        db_column="Unit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    weight = models.DecimalField(
        db_column="Weight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    length = models.DecimalField(
        db_column="Length", max_digits=19, decimal_places=7, blank=True, null=True
    )
    variableweight = models.BooleanField(db_column="VariableWeight")
    variablelength = models.BooleanField(db_column="VariableLength")
    specification = models.CharField(
        db_column="Specification",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    productpricecategory = models.CharField(
        db_column="ProductPriceCategory",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pricebycategory = models.BooleanField(db_column="PriceByCategory")

    leadtime = models.IntegerField(db_column="LeadTime", blank=True, null=True)
    salescategory = models.CharField(
        db_column="SalesCategory",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    discontinued = models.BooleanField(db_column="Discontinued")
    costmethod = models.CharField(
        db_column="CostMethod",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    producttype = models.CharField(
        db_column="ProductType",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    inventorycontroltype = models.CharField(
        db_column="InventoryControlType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    assemblytype = models.CharField(
        db_column="AssemblyType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    countcycle = models.CharField(
        db_column="CountCycle",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    createdby = models.CharField(
        db_column="CreatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    createddate = models.DateTimeField(db_column="CreatedDate", blank=True, null=True)
    updatedby = models.CharField(
        db_column="UpdatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    updateddate = models.DateTimeField(db_column="UpdatedDate", blank=True, null=True)
    status = models.BooleanField(db_column="Status")
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    popup = models.BooleanField(db_column="Popup")
    ponote = models.TextField(
        db_column="PONote",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    popopup = models.BooleanField(db_column="POPopup")
    color = models.CharField(
        db_column="Color",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    height = models.DecimalField(
        db_column="Height", max_digits=19, decimal_places=7, blank=True, null=True
    )
    size = models.CharField(
        db_column="Size",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    variableheight = models.BooleanField(db_column="VariableHeight")
    variablevolume = models.BooleanField(db_column="VariableVolume")
    variablewidth = models.BooleanField(db_column="VariableWidth")
    volume = models.DecimalField(
        db_column="Volume", max_digits=19, decimal_places=7, blank=True, null=True
    )
    width = models.DecimalField(
        db_column="Width", max_digits=19, decimal_places=7, blank=True, null=True
    )
    techspec = models.TextField(
        db_column="TechSpec",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    webaddress = models.TextField(
        db_column="WebAddress",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    altdescription = models.TextField(
        db_column="AltDescription",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    description = models.TextField(
        db_column="Description",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    notforresale = models.BooleanField(db_column="NotForResale")
    maintaininventorytype = models.IntegerField(db_column="MaintainInventoryType")
    availonweb = models.BooleanField(db_column="AvailOnWeb")
    productpicture = models.BinaryField(
        db_column="ProductPicture", blank=True, null=True
    )
    shipcompletelots = models.BooleanField(db_column="ShipCompleteLots")
    altweight = models.DecimalField(
        db_column="AltWeight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    altlength = models.DecimalField(
        db_column="AltLength", max_digits=19, decimal_places=7, blank=True, null=True
    )
    altheight = models.DecimalField(
        db_column="AltHeight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    altwidth = models.DecimalField(
        db_column="AltWidth", max_digits=19, decimal_places=7, blank=True, null=True
    )
    altvolume = models.DecimalField(
        db_column="AltVolume", max_digits=19, decimal_places=7, blank=True, null=True
    )
    altunitsperpalletlayer = models.DecimalField(
        db_column="AltUnitsPerPalletLayer",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    palletlayers = models.DecimalField(
        db_column="PalletLayers", max_digits=19, decimal_places=7, blank=True, null=True
    )
    innerpackqty = models.DecimalField(
        db_column="InnerPackQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    outerpackqty = models.DecimalField(
        db_column="OuterPackQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    discountable = models.BooleanField(db_column="Discountable")
    salesunit = models.CharField(
        db_column="SalesUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    purchaseunit = models.CharField(
        db_column="PurchaseUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    packageunit = models.CharField(
        db_column="PackageUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    landedcostfactor = models.DecimalField(
        db_column="LandedCostFactor",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    productpicture256 = models.BinaryField(
        db_column="ProductPicture256", blank=True, null=True
    )

    def __str__(self):
        return "%s: %s" % self.productid, self.description[:30]

    @property
    def avgcost(self):
        cost = 0
        for wh in self.warehouses.all():
            if wh.summary.avgcost and wh.summary.avgcost > cost:
                cost = wh.summary.avgcost
        if cost > 0:
            return cost

    @property
    def anycost(self):
        cost = 0
        for wh in self.warehouses.all():

            if wh.summary.avgcost and wh.summary.avgcost > cost:
                cost = wh.summary.avgcost

            if wh.summary.lastcost and wh.summary.lastcost > cost:
                cost = wh.summary.lastcost

        if cost == 0:
            # Defer to vendor cost
            cost = self.suppliers.get(preferred=True).vendorprice

        if cost == 0:
            raise Exception("Product without a cost")

        return cost

    @property
    def mgmtcost(self):
        cost = 0
        for wh in self.warehouses.all():
            if wh.summary.mgmtcost and wh.summary.mgmtcost > cost:
                cost = wh.summary.mgmtcost
        if cost > 0:
            return cost

    @property
    def WebPrice(self):
        """Generates a price to upload to our web store"""
        price = 0
        for p in self.prices.all():
            finalprice = p.CalculatedPrice

            if finalprice and finalprice > price:
                price = finalprice
        return price

    class Meta:
        managed = False
        db_table = "tbproduct"


class Tbproductwarehouse(models.Model):
    guidproductwarehouse = models.CharField(
        db_column="GUIDProductWarehouse", primary_key=True, max_length=36
    )
    product = models.ForeignKey(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="warehouses",
    )
    warehouse = models.ForeignKey(
        Tbwarehouse,
        on_delete=models.PROTECT,
        db_column="GUIDWarehouse",
        related_name="product_warehouses",
    )
    qtyreserved = models.DecimalField(
        db_column="QtyReserved", max_digits=19, decimal_places=7, blank=True, null=True
    )
    location = models.CharField(
        db_column="Location",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lastcost = models.DecimalField(
        db_column="LastCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    stdcost = models.DecimalField(
        db_column="StdCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    unitcost = models.DecimalField(
        db_column="UnitCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    value = models.DecimalField(
        db_column="Value", max_digits=19, decimal_places=4, blank=True, null=True
    )
    reorderpoint = models.DecimalField(
        db_column="ReorderPoint", max_digits=19, decimal_places=7, blank=True, null=True
    )
    stockinglevel = models.DecimalField(
        db_column="StockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    qtytoreorder = models.DecimalField(
        db_column="QtyToReorder", max_digits=19, decimal_places=7, blank=True, null=True
    )
    lastcountdate = models.DateTimeField(
        db_column="LastCountDate", blank=True, null=True
    )
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    primarylocationstockinglevel = models.DecimalField(
        db_column="PrimaryLocationStockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", max_length=36, blank=True, null=True
    )
    reorderincludeinpo = models.BooleanField(db_column="ReorderIncludeInPO")
    reorderguidvendor = models.CharField(
        db_column="ReorderGUIDVendor", max_length=36, blank=True, null=True
    )
    reorderunit = models.CharField(
        db_column="ReorderUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    reorderqty = models.DecimalField(
        db_column="ReorderQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    reordercost = models.DecimalField(
        db_column="ReorderCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    reordervendorproductid = models.CharField(
        db_column="ReorderVendorProductID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    buildqty = models.DecimalField(
        db_column="BuildQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    buildchecked = models.BooleanField(db_column="BuildChecked")
    deleted = models.BooleanField(db_column="Deleted")

    class Meta:
        managed = False
        db_table = "tbproductwarehouse"
        unique_together = (("guidproduct", "guidwarehouse"),)


class Tbproductsupplier(models.Model):
    guidproductsupplier = models.CharField(
        db_column="GUIDProductSupplier", primary_key=True, max_length=36
    )

    product = models.ForeignKey(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="suppliers",
    )

    vendor = models.ForeignKey(
        Tbvendor, on_delete=models.PROTECT, db_column="GUIDVendor"
    )

    vendorproductid = models.CharField(
        db_column="VendorProductID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    unit = models.CharField(
        db_column="Unit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    preferred = models.BooleanField(db_column="Preferred")
    leadtime = models.IntegerField(db_column="LeadTime", blank=True, null=True)
    lastprice = models.DecimalField(
        db_column="LastPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    vendorprice = models.DecimalField(
        db_column="VendorPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    lastreceiptdate = models.DateTimeField(
        db_column="LastReceiptDate", blank=True, null=True
    )
    lastreceiptqty = models.DecimalField(
        db_column="LastReceiptQty",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lastreceiptunit = models.CharField(
        db_column="LastReceiptUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "tbproductsupplier"
        unique_together = (("guidproduct", "guidvendor", "vendorproductid"),)


class Tbproductprice(models.Model):
    guidproductprice = models.CharField(
        db_column="GUIDProductPrice", primary_key=True, max_length=36
    )
    product = models.ForeignKey(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="prices",
    )
    guidcustomer = models.CharField(
        db_column="GUIDCustomer", max_length=36, blank=True, null=True
    )
    guidcurrency = models.CharField(
        db_column="GUIDCurrency", max_length=36, blank=True, null=True
    )
    contractid = models.CharField(
        db_column="ContractID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    productpricecategory = models.CharField(
        db_column="ProductPriceCategory",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pricecode = models.CharField(
        db_column="PriceCode",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    effectivedate = models.DateTimeField(
        db_column="EffectiveDate", blank=True, null=True
    )
    expirationdate = models.DateTimeField(
        db_column="ExpirationDate", blank=True, null=True
    )
    lowqty = models.DecimalField(
        db_column="LowQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    highqty = models.DecimalField(
        db_column="HighQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    pricetype = models.CharField(
        db_column="PriceType",
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        db_column="Price", max_digits=19, decimal_places=7, blank=True, null=True
    )
    priceunit = models.CharField(
        db_column="PriceUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    taxincluded = models.BooleanField(db_column="TaxIncluded")
    discountable = models.BooleanField(db_column="Discountable")
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    @property
    def CalculatedPrice(self):
        if self.pricetype == "P":
            return self.price
        elif self.pricetype == "C%":
            # avg cost + %
            base = self.product.avgcost
            if not base:

                if self.product.suppliers.filter(preferred=True).count() == 1:
                    # If product has a preferred supplier, use it
                    pps = self.product.suppliers.get(preferred=True)
                    base = pps.lastprice or pps.vendorprice
                else:
                    # Otherwise, get the most expensive one
                    pps = self.product.suppliers.order_by("-lastprice").first()
                    base = pps.lastprice or pps.vendorprice

            if base is not None:
                hike = (base * self.price) / 100
                return base + hike
            else:
                raise Exception("No cost to calculate price")
            
        elif self.pricetype == "S%":
            # mgmt cost + %
            base = self.product.mgmtcost
            hike = (self.product.mgmtcost * self.price) / 100
            return base + hike

    def __str__(self):
        if self.pricetype == "P":
            return "Static $%s" % self.price
        elif "%" in self.pricetype:
            return "PCT Priced %s%%" % self.price
        else:
            return "Unknown %s" % self.price

    class Meta:
        managed = False
        db_table = "tbproductprice"


class Productwarehousesummary(models.Model):
    productwarehouse = models.OneToOneField(
        "Tbproductwarehouse",
        on_delete=models.PROTECT,
        db_column="GUIDProductWarehouse",
        primary_key=True,
        related_name="summary",
    )

    product = models.ForeignKey(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="whsummaries",
    )

    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36, blank=True, null=True
    )
    warehouse = models.CharField(
        db_column="Warehouse", max_length=6, blank=True, null=True
    )
    warehousedescription = models.CharField(
        db_column="WarehouseDescription", max_length=50, blank=True, null=True
    )
    productid = models.CharField(db_column="ProductID", max_length=159)
    qtyreserved = models.DecimalField(
        db_column="QtyReserved", max_digits=19, decimal_places=7, blank=True, null=True
    )
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", max_length=36, blank=True, null=True
    )
    location = models.CharField(
        db_column="Location", max_length=80, blank=True, null=True
    )
    primarylocationstockinglevel = models.DecimalField(
        db_column="PrimaryLocationStockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    lastcost = models.DecimalField(
        db_column="LastCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    mgmtcost = models.DecimalField(
        db_column="MgmtCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    standardcost = models.DecimalField(
        db_column="StandardCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    reorderpoint = models.DecimalField(
        db_column="ReorderPoint", max_digits=19, decimal_places=7, blank=True, null=True
    )
    stockinglevel = models.DecimalField(
        db_column="StockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    qtytoreorder = models.DecimalField(
        db_column="QtyToReorder", max_digits=19, decimal_places=7, blank=True, null=True
    )
    lastcountdate = models.DateTimeField(
        db_column="LastCountDate", blank=True, null=True
    )
    note = models.TextField(db_column="Note", blank=True, null=True)
    qtyonhand = models.DecimalField(
        db_column="QtyOnHand", max_digits=38, decimal_places=7, blank=True, null=True
    )
    onhandvalue = models.DecimalField(
        db_column="OnHandValue", max_digits=19, decimal_places=4, blank=True, null=True
    )
    avgcost = models.DecimalField(
        db_column="AvgCost", max_digits=38, decimal_places=16, blank=True, null=True
    )
    quantityonpo = models.DecimalField(
        db_column="QuantityOnPO", max_digits=38, decimal_places=7, blank=True, null=True
    )
    quantityonreturn = models.DecimalField(
        db_column="QuantityOnReturn",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    quantityonorder = models.DecimalField(
        db_column="QuantityOnOrder",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    amountonorder = models.DecimalField(
        db_column="AmountOnOrder",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    qtyordered = models.DecimalField(
        db_column="QtyOrdered", max_digits=38, decimal_places=7, blank=True, null=True
    )
    qtybooked = models.DecimalField(
        db_column="QtyBooked", max_digits=38, decimal_places=7, blank=True, null=True
    )
    qtyscheduled = models.DecimalField(
        db_column="QtyScheduled", max_digits=38, decimal_places=7, blank=True, null=True
    )
    qtybackordered = models.DecimalField(
        db_column="QtyBackordered",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    qtyspecialorder = models.DecimalField(
        db_column="QtySpecialOrder",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    unpostedcomponentquantity = models.DecimalField(
        db_column="UnpostedComponentQuantity",
        max_digits=38,
        decimal_places=13,
        blank=True,
        null=True,
    )
    unpostedassemblyquantity = models.DecimalField(
        db_column="UnpostedAssemblyQuantity",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    unpostedtransferquantity = models.DecimalField(
        db_column="UnpostedTransferQuantity",
        max_digits=38,
        decimal_places=7,
        blank=True,
        null=True,
    )
    qtyorderedamount = models.DecimalField(
        db_column="QtyOrderedAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    qtyschedamount = models.DecimalField(
        db_column="QtySchedAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    allocated = models.DecimalField(
        db_column="Allocated", max_digits=38, decimal_places=7, blank=True, null=True
    )
    available = models.DecimalField(
        db_column="Available", max_digits=38, decimal_places=7, blank=True, null=True
    )
    lasttransactiondate = models.DateTimeField(
        db_column="LastTransactionDate", blank=True, null=True
    )
    qtyrequired = models.DecimalField(
        db_column="QtyRequired", max_digits=38, decimal_places=7, blank=True, null=True
    )
    stdcost = models.DecimalField(
        db_column="StdCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    producttype = models.CharField(
        db_column="ProductType", max_length=8, blank=True, null=True
    )
    salescategory = models.CharField(
        db_column="SalesCategory", max_length=8, blank=True, null=True
    )
    description = models.CharField(
        db_column="Description", max_length=4095, blank=True, null=True
    )
    unit = models.CharField(db_column="Unit", max_length=5, blank=True, null=True)
    productclassid = models.CharField(
        db_column="ProductClassID", max_length=8, blank=True, null=True
    )
    productclassdescription = models.CharField(
        db_column="ProductClassDescription", max_length=50, blank=True, null=True
    )
    expectedreceiptdate = models.DateTimeField(
        db_column="ExpectedReceiptDate", blank=True, null=True
    )
    reorderincludeinpo = models.BooleanField(db_column="ReorderIncludeInPO")
    reorderguidvendor = models.CharField(
        db_column="ReorderGUIDVendor", max_length=36, blank=True, null=True
    )
    reorderunit = models.CharField(
        db_column="ReorderUnit", max_length=5, blank=True, null=True
    )
    reordercost = models.DecimalField(
        db_column="ReorderCost", max_digits=19, decimal_places=7, blank=True, null=True
    )
    reorderqty = models.DecimalField(
        db_column="ReorderQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    reordervendorproductid = models.CharField(
        db_column="ReorderVendorProductID", max_length=25, blank=True, null=True
    )
    buildqty = models.DecimalField(
        db_column="BuildQty", max_digits=19, decimal_places=7, blank=True, null=True
    )
    buildchecked = models.BooleanField(db_column="BuildChecked")
    deleted = models.BooleanField(db_column="Deleted")

    class Meta:
        managed = False
        db_table = "productwarehousesummary"


class Tbpo(models.Model):
    guidpo = models.CharField(db_column="GUIDPO", primary_key=True, max_length=36)
    vendor = models.ForeignKey(
        Tbvendor, on_delete=models.PROTECT, db_column="GUIDVendor"
    )
    order = models.ForeignKey(Tborders, on_delete=models.PROTECT, db_column="GUIDOrder")

    guidapaccount = models.CharField(
        db_column="GUIDAPAccount", max_length=36, blank=True, null=True
    )
    approvedby = models.CharField(
        db_column="ApprovedBy",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    approvedbyid = models.CharField(
        db_column="ApprovedByID",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    approvedinvoicedate = models.DateTimeField(
        db_column="ApprovedInvoiceDate", blank=True, null=True
    )
    approvedinvoicediscountamount = models.DecimalField(
        db_column="ApprovedInvoiceDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    approvedinvoicediscountdate = models.DateTimeField(
        db_column="ApprovedInvoiceDiscountDate", blank=True, null=True
    )
    approvedinvoiceduedate = models.DateTimeField(
        db_column="ApprovedInvoiceDueDate", blank=True, null=True
    )
    approvedinvoicenumber = models.CharField(
        db_column="ApprovedInvoiceNumber",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    dateapproved = models.DateTimeField(db_column="DateApproved", blank=True, null=True)
    datecompleted = models.DateTimeField(
        db_column="DateCompleted", blank=True, null=True
    )
    dateentered = models.DateTimeField(db_column="DateEntered", blank=True, null=True)
    dateissued = models.DateTimeField(db_column="DateIssued", blank=True, null=True)
    dateprinted = models.DateTimeField(db_column="DatePrinted", blank=True, null=True)
    daterequested = models.DateTimeField(
        db_column="DateRequested", blank=True, null=True
    )
    dontshipafter = models.DateTimeField(
        db_column="DontShipAfter", blank=True, null=True
    )
    dontshipbefore = models.DateTimeField(
        db_column="DontShipBefore", blank=True, null=True
    )
    enteredby = models.CharField(
        db_column="EnteredBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    fob = models.CharField(
        db_column="FOB",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    issuedby = models.CharField(
        db_column="IssuedBy",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    notes = models.TextField(
        db_column="Notes",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ponumber = models.CharField(
        db_column="PONumber",
        unique=True,
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    postatus = models.CharField(
        db_column="POStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    printed = models.BooleanField(db_column="Printed")
    promiseddate = models.DateTimeField(db_column="PromisedDate", blank=True, null=True)
    guidpurchaseaccount = models.CharField(
        db_column="GUIDPurchaseAccount", max_length=36, blank=True, null=True
    )
    readytoprint = models.BooleanField(db_column="ReadyToPrint")
    requestdate = models.DateTimeField(db_column="RequestDate", blank=True, null=True)
    requestedby = models.CharField(
        db_column="RequestedBy",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    requestedbyid = models.CharField(
        db_column="RequestedByID",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoaddress1 = models.CharField(
        db_column="ShipToAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoaddress2 = models.CharField(
        db_column="ShipToAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoaddress3 = models.CharField(
        db_column="ShipToAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoaddress4 = models.CharField(
        db_column="ShipToAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoattention = models.CharField(
        db_column="ShipToAttention",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptocity = models.CharField(
        db_column="ShipToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptocountry = models.CharField(
        db_column="ShipToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoname = models.CharField(
        db_column="ShipToName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptooverride = models.BooleanField(db_column="ShipToOverride")
    shiptostate = models.CharField(
        db_column="ShipToState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptozip = models.CharField(
        db_column="ShipToZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipvia = models.CharField(
        db_column="ShipVia",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    specialinstructions = models.TextField(
        db_column="SpecialInstructions",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    statuschangedby = models.CharField(
        db_column="StatusChangedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    statusdate = models.DateTimeField(db_column="StatusDate", blank=True, null=True)
    subtotalamountapproved = models.DecimalField(
        db_column="SubTotalAmountApproved",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    suppliername = models.CharField(
        db_column="SupplierName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplieroverride = models.BooleanField(db_column="SupplierOverride")
    supplieraddress1 = models.CharField(
        db_column="SupplierAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplieraddress2 = models.CharField(
        db_column="SupplierAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplieraddress3 = models.CharField(
        db_column="SupplierAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplieraddress4 = models.CharField(
        db_column="SupplierAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    suppliercity = models.CharField(
        db_column="SupplierCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierstate = models.CharField(
        db_column="SupplierState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierzip = models.CharField(
        db_column="SupplierZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    suppliercountry = models.CharField(
        db_column="SupplierCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbilladdress1 = models.CharField(
        db_column="SupplierBillAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbilladdress2 = models.CharField(
        db_column="SupplierBillAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbilladdress3 = models.CharField(
        db_column="SupplierBillAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbilladdress4 = models.CharField(
        db_column="SupplierBillAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbillcity = models.CharField(
        db_column="SupplierBillCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbillstate = models.CharField(
        db_column="SupplierBillState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbillzip = models.CharField(
        db_column="SupplierBillZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierbillcountry = models.CharField(
        db_column="SupplierBillCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidterms = models.CharField(
        db_column="GUIDTerms", max_length=36, blank=True, null=True
    )
    totalamount = models.DecimalField(
        db_column="TotalAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalamountapproved = models.DecimalField(
        db_column="TotalAmountApproved",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    totalamountinvoiced = models.DecimalField(
        db_column="TotalAmountInvoiced",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    totalamountoutstanding = models.DecimalField(
        db_column="TotalAmountOutstanding",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    totalamountreceived = models.DecimalField(
        db_column="TotalAmountReceived",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    totalotheramount = models.DecimalField(
        db_column="TotalOtherAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    type = models.CharField(
        db_column="Type",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidvendortype = models.CharField(
        db_column="GUIDVendorType", max_length=36, blank=True, null=True
    )
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36, blank=True, null=True
    )
    reference = models.CharField(
        db_column="Reference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    relateddocument = models.CharField(
        db_column="RelatedDocument",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    vendcustid = models.CharField(
        db_column="VendCustID",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contact = models.CharField(
        db_column="Contact",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        db_column="Phone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    fax = models.CharField(
        db_column="FAX",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    email = models.CharField(
        db_column="Email",
        max_length=253,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    salestax = models.DecimalField(
        db_column="SalesTax", max_digits=19, decimal_places=4, blank=True, null=True
    )
    salestaxamountapproved = models.DecimalField(
        db_column="SalesTaxAmountApproved",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=19, decimal_places=7
    )
    taxincluded = models.BooleanField(db_column="TaxIncluded")
    field_exclapr = models.BooleanField(db_column="_EXCLAPR")
    suppliersyncdate = models.DateTimeField(
        db_column="SupplierSyncDate", blank=True, null=True
    )
    supplierstatus = models.CharField(
        db_column="SupplierStatus",
        max_length=10,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "tbpo"


class Tbpodetail(models.Model):
    guidpodetail = models.CharField(
        db_column="GUIDPODetail", primary_key=True, max_length=36
    )
    po = models.ForeignKey(Tbpo, on_delete=models.PROTECT, db_column="GUIDPO")
    amountapproved = models.DecimalField(
        db_column="AmountApproved",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    complete = models.BooleanField(db_column="Complete")
    description = models.TextField(
        db_column="Description",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidglexpenseaccount = models.CharField(
        db_column="GUIDGLExpenseAccount", max_length=36, blank=True, null=True
    )
    glexpenseaccountdescription = models.CharField(
        db_column="GLExpenseAccountDescription",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lineamount = models.DecimalField(
        db_column="LineAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    displayamount = models.DecimalField(
        db_column="DisplayAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    linenumber = models.IntegerField(db_column="LineNumber")
    linetype = models.CharField(
        db_column="LineType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    notes = models.TextField(
        db_column="Notes",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    priceinvoiced = models.DecimalField(
        db_column="PriceInvoiced",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    pricerequested = models.DecimalField(
        db_column="PriceRequested",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    displayprice = models.DecimalField(
        db_column="DisplayPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    product = models.ForeignKey(
        "Tbproduct", on_delete=models.PROTECT, db_column="GUIDProduct"
    )
    productid = models.CharField(
        db_column="ProductID",
        max_length=159,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    quantityinvoiceapproved = models.DecimalField(
        db_column="QuantityInvoiceApproved",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    quantityordered = models.DecimalField(
        db_column="QuantityOrdered",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    specialinstructions = models.TextField(
        db_column="SpecialInstructions",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    supplierproductid = models.CharField(
        db_column="SupplierProductID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    unit = models.CharField(
        db_column="Unit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    guidorderdetail = models.CharField(
        db_column="GUIDOrderDetail", max_length=36, blank=True, null=True
    )
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )
    salestax = models.DecimalField(
        db_column="SalesTax", max_digits=19, decimal_places=4, blank=True, null=True
    )
    displayunit = models.CharField(
        db_column="DisplayUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    displayunitfactor = models.DecimalField(
        db_column="DisplayUnitFactor",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    landedcostsession = models.IntegerField(
        db_column="LandedCostSession", blank=True, null=True
    )
    salestaxamountapproved = models.DecimalField(
        db_column="SalesTaxAmountApproved",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "tbpodetail"


class Tbproductalt(models.Model):
    guidproductalt = models.CharField(
        db_column="GUIDProductAlt", primary_key=True, max_length=36
    )  # Field name made lowercase.
    product = models.ForeignKey(
        "Tbproduct",
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="alt_ids",
    )
    altproductid = models.CharField(
        db_column="AltProductID",
        max_length=159,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    xreftype = models.CharField(
        db_column="XrefType", max_length=3, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )  # Field name made lowercase.
    guidlink = models.CharField(
        db_column="GUIDLink", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    primary = models.BooleanField(db_column="Primary")  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tbproductalt"


class Tbproductcomponent(models.Model):
    guidproductcomponent = models.CharField(
        db_column="GUIDProductComponent", primary_key=True, max_length=36
    )  # Field name made lowercase.
    product = models.ForeignKey(
        "Tbproduct",
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="components",
    )
    componenttype = models.CharField(
        db_column="ComponentType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    componentguidproduct = models.CharField(
        db_column="ComponentGUIDProduct", max_length=36
    )  # Field name made lowercase.
    guidcomponentwarehouse = models.CharField(
        db_column="GUIDComponentWarehouse", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    quantity = models.DecimalField(
        db_column="Quantity", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    variablequantity = models.BooleanField(
        db_column="VariableQuantity"
    )  # Field name made lowercase.
    cost = models.DecimalField(
        db_column="Cost", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    sequence = models.IntegerField(
        db_column="Sequence", blank=True, null=True
    )  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tbproductcomponent"

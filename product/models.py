from portal.models import *


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

    @property
    def avgcost(self):
        cost = 0
        for wh in self.warehouses.all():
            if wh.summary.avgcost and wh.summary.avgcost > cost:
                cost = wh.summary.avgcost
        if cost > 0:
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
        price = 0
        for p in self.prices.all():
            if p.FinalPrice > price:
                price = p.FinalPrice
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
    remotestock = models.IntegerField(db_column="RemoteStock", blank=True, null=True)
    lastsync = models.DateTimeField(db_column="LastSync", blank=True, null=True)
    remoteid = models.CharField(
        db_column="RemoteID",
        max_length=250,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    def set_remote_stock(self, newvalue):
        logger.info(
            updated="remotestock",
            remotestock=newvalue,
            productid=self.product.productid,
            lastsync=hf.format_timespan(timezone.now() - self.lastsync),
        )

        self.remotestock = newvalue
        self.lastsync = timezone.now()

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
    def FinalPrice(self):
        if self.pricetype == "P":
            return self.price
        elif self.pricetype == "C%":
            # avg cost + %
            base = self.product.avgcost
            hike = (self.product.avgcost * self.price) / 100
            return base + hike
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

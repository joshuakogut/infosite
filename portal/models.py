from django.db import models
from django.db.models import Q
from django.utils import timezone
import humanfriendly as hf
from portal import Logger

logger = Logger("sync.trailgear.orders")


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
        Tbproductclass, on_delete=models.PROTECT, db_column="GUIDProductClass"
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

    class Meta:
        managed = False
        db_table = "tbproduct"


class Tbvendor(models.Model):
    guidvendor = models.CharField(
        db_column="GUIDVendor", primary_key=True, max_length=36
    )
    vendorlistid = models.CharField(
        db_column="VendorListID",
        unique=True,
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    vendorid = models.CharField(
        db_column="VendorID",
        unique=True,
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    name = models.CharField(
        db_column="Name",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    salutation = models.CharField(
        db_column="Salutation",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    firstname = models.CharField(
        db_column="FirstName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    middlename = models.CharField(
        db_column="MiddleName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lastname = models.CharField(
        db_column="LastName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    suffix = models.CharField(
        db_column="Suffix",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address1 = models.CharField(
        db_column="Address1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address2 = models.CharField(
        db_column="Address2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address3 = models.CharField(
        db_column="Address3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address4 = models.CharField(
        db_column="Address4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    city = models.CharField(
        db_column="City",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    state = models.CharField(
        db_column="State",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    zip = models.CharField(
        db_column="Zip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    country = models.CharField(
        db_column="Country",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipaddress1 = models.CharField(
        db_column="ShipAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipaddress2 = models.CharField(
        db_column="ShipAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipaddress3 = models.CharField(
        db_column="ShipAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipaddress4 = models.CharField(
        db_column="ShipAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipcity = models.CharField(
        db_column="ShipCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipstate = models.CharField(
        db_column="ShipState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipzip = models.CharField(
        db_column="ShipZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipcountry = models.CharField(
        db_column="ShipCountry",
        max_length=255,
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
    mobile = models.CharField(
        db_column="Mobile",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pager = models.CharField(
        db_column="Pager",
        max_length=21,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    altphone = models.CharField(
        db_column="AltPhone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    fax = models.CharField(
        db_column="Fax",
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
    contact = models.CharField(
        db_column="Contact",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    altcontact = models.CharField(
        db_column="AltContact",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    nameoncheck = models.CharField(
        db_column="NameOnCheck",
        max_length=100,
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
    accountnumber = models.CharField(
        db_column="AccountNumber",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    creditlimit = models.DecimalField(
        db_column="CreditLimit", max_digits=19, decimal_places=4, blank=True, null=True
    )
    vendortaxident = models.CharField(
        db_column="VendorTaxIdent",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    isvendoreligiblefor1099 = models.BooleanField(db_column="IsVendorEligibleFor1099")
    balance = models.DecimalField(
        db_column="Balance", max_digits=19, decimal_places=4, blank=True, null=True
    )
    vendcustid = models.CharField(
        db_column="VendCustID",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    istaxontax = models.BooleanField(db_column="IsTaxOnTax")
    active = models.BooleanField(db_column="Active")

    timecreated = models.DateTimeField(db_column="TimeCreated", blank=True, null=True)
    timemodified = models.DateTimeField(db_column="TimeModified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tbvendor"


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
        max_length=50,
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
    )  # Field name made lowercase.
    product = models.ForeignKey(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="GUIDProduct",
        related_name="prices",
    )
    guidcustomer = models.CharField(
        db_column="GUIDCustomer", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidcurrency = models.CharField(
        db_column="GUIDCurrency", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    contractid = models.CharField(
        db_column="ContractID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    productpricecategory = models.CharField(
        db_column="ProductPriceCategory",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    pricecode = models.CharField(
        db_column="PriceCode",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    effectivedate = models.DateTimeField(
        db_column="EffectiveDate", blank=True, null=True
    )  # Field name made lowercase.
    expirationdate = models.DateTimeField(
        db_column="ExpirationDate", blank=True, null=True
    )  # Field name made lowercase.
    lowqty = models.DecimalField(
        db_column="LowQty", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    highqty = models.DecimalField(
        db_column="HighQty", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    pricetype = models.CharField(
        db_column="PriceType",
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    price = models.DecimalField(
        db_column="Price", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    priceunit = models.CharField(
        db_column="PriceUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    taxincluded = models.BooleanField(
        db_column="TaxIncluded"
    )  # Field name made lowercase.
    discountable = models.BooleanField(
        db_column="Discountable"
    )  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    def __str__(self):
        if self.pricetype == "P":
            return "Static $%s" % self.price
        elif "%" in self.pricetype:
            "PCT Priced %s%%" % self.price
        else:
            "Unknown %s" % self.price

    class Meta:
        managed = False
        db_table = "tbproductprice"


class Tbwarehouse(models.Model):
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", primary_key=True, max_length=36
    )
    warehouseid = models.CharField(
        db_column="WarehouseID",
        unique=True,
        max_length=6,
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
    associatedguidbranch = models.CharField(
        db_column="AssociatedGUIDBranch", max_length=36, blank=True, null=True
    )
    guidinventoryaccount = models.CharField(
        db_column="GUIDInventoryAccount", max_length=36, blank=True, null=True
    )
    guidpurchaseaccount = models.CharField(
        db_column="GUIDPurchaseAccount", max_length=36, blank=True, null=True
    )
    guidadjustmentaccount = models.CharField(
        db_column="GUIDAdjustmentAccount", max_length=36, blank=True, null=True
    )
    guidassemblylaboraccount = models.CharField(
        db_column="GUIDAssemblyLaborAccount", max_length=36, blank=True, null=True
    )
    guidassemblyothercostaccount = models.CharField(
        db_column="GUIDAssemblyOtherCostAccount", max_length=36, blank=True, null=True
    )
    guidissueaccount = models.CharField(
        db_column="GUIDIssueAccount", max_length=36, blank=True, null=True
    )
    guidnoninvoffsetaccount = models.CharField(
        db_column="GUIDNonInvOffsetAccount", max_length=36, blank=True, null=True
    )
    guidlaboroffsetaccount = models.CharField(
        db_column="GUIDLaborOffsetAccount", max_length=36, blank=True, null=True
    )
    guidotherchargeoffsetaccount = models.CharField(
        db_column="GUIDOtherChargeOffsetAccount", max_length=36, blank=True, null=True
    )
    guidshippingoffsetaccount = models.CharField(
        db_column="GUIDShippingOffsetAccount", max_length=36, blank=True, null=True
    )
    guidlandedcostoffsetaccount = models.CharField(
        db_column="GUIDLandedCostOffsetAccount", max_length=36, blank=True, null=True
    )
    name = models.CharField(
        db_column="Name",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoattentionof = models.CharField(
        db_column="ShipToAttentionOf",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address1 = models.CharField(
        db_column="Address1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address2 = models.CharField(
        db_column="Address2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address3 = models.CharField(
        db_column="Address3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    address4 = models.CharField(
        db_column="Address4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    email = models.CharField(
        db_column="EMail",
        max_length=253,
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
    fob = models.CharField(
        db_column="FOB",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    maintaininventory = models.BooleanField(db_column="MaintainInventory")
    laborcost = models.DecimalField(
        db_column="LaborCost", max_digits=19, decimal_places=4, blank=True, null=True
    )
    active = models.BooleanField(db_column="Active")
    city = models.CharField(
        db_column="City",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    country = models.CharField(
        db_column="Country",
        max_length=255,
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
    phone = models.CharField(
        db_column="Phone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    state = models.CharField(
        db_column="State",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    zip = models.CharField(
        db_column="Zip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidgainlossaccount = models.CharField(
        db_column="GUIDGainLossAccount", max_length=36, blank=True, null=True
    )
    guidpartner = models.CharField(
        db_column="GUIDPartner", max_length=36, blank=True, null=True
    )
    layout = models.TextField(
        db_column="Layout",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    allowpicklists = models.BooleanField(db_column="AllowPicklists")

    class Meta:
        managed = False
        db_table = "tbwarehouse"


class Tbpo(models.Model):
    guidpo = models.CharField(db_column="GUIDPO", primary_key=True, max_length=36)
    vendor = models.ForeignKey(
        Tbvendor, on_delete=models.PROTECT, db_column="GUIDVendor"
    )
    order = models.ForeignKey(
        "Tborders", on_delete=models.PROTECT, db_column="GUIDOrder"
    )

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
        Tbproduct, on_delete=models.PROTECT, db_column="GUIDProduct"
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


class Tbcustomer(models.Model):
    guidcustomer = models.CharField(
        db_column="GUIDCustomer", primary_key=True, max_length=36
    )  # Field name made lowercase.
    custlistid = models.CharField(
        db_column="CustListID",
        unique=True,
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    custid = models.CharField(
        db_column="CustId", max_length=500, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )  # Field name made lowercase.
    guidparent = models.CharField(
        db_column="GUIDParent", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    method = models.IntegerField(
        db_column="Method", blank=True, null=True
    )  # Field name made lowercase.
    guidcustomertype = models.CharField(
        db_column="GUIDCustomerType", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    companyname = models.CharField(
        db_column="CompanyName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="Name",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    salutation = models.CharField(
        db_column="Salutation",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    firstname = models.CharField(
        db_column="FirstName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    middlename = models.CharField(
        db_column="MiddleName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lastname = models.CharField(
        db_column="LastName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    suffix = models.CharField(
        db_column="Suffix",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    address = models.CharField(
        db_column="Address",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    address2 = models.CharField(
        db_column="Address2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    address3 = models.CharField(
        db_column="Address3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    address4 = models.CharField(
        db_column="Address4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    city = models.CharField(
        db_column="City",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    state = models.CharField(
        db_column="State",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    zip = models.CharField(
        db_column="Zip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    country = models.CharField(
        db_column="Country",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    phone = models.CharField(
        db_column="Phone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    phonedesc = models.CharField(
        db_column="PhoneDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    fax = models.CharField(
        db_column="Fax",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    faxdesc = models.CharField(
        db_column="FaxDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    email = models.CharField(
        db_column="Email",
        max_length=253,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    emaildesc = models.CharField(
        db_column="EmailDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    altphone = models.CharField(
        db_column="AltPhone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    altphonedesc = models.CharField(
        db_column="AltPhoneDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mobile = models.CharField(
        db_column="Mobile",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mobiledesc = models.CharField(
        db_column="MobileDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    pager = models.CharField(
        db_column="Pager",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    pagerdesc = models.CharField(
        db_column="PagerDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidsalesperson = models.CharField(
        db_column="GUIDSalesperson", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    statesalestaxid = models.CharField(
        db_column="StateSalesTaxId",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    taxexemptionreasonid = models.IntegerField(
        db_column="TaxExemptionReasonID", blank=True, null=True
    )  # Field name made lowercase.
    taxincluded = models.BooleanField(
        db_column="TaxIncluded"
    )  # Field name made lowercase.
    guidterms = models.CharField(
        db_column="GUIDTerms", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    locationid = models.CharField(
        db_column="LocationId",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    creditlimit = models.DecimalField(
        db_column="CreditLimit", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    credithold = models.BooleanField(
        db_column="CreditHold"
    )  # Field name made lowercase.
    preferredpaymentmethod = models.CharField(
        db_column="PreferredPaymentMethod", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    status = models.BooleanField(
        db_column="Status", blank=True, null=True
    )  # Field name made lowercase.
    ccnumber = models.CharField(
        db_column="CCNumber",
        max_length=64,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccdisplaynumber = models.CharField(
        db_column="CCDisplayNumber",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccexpmonth = models.IntegerField(
        db_column="CCExpMonth", blank=True, null=True
    )  # Field name made lowercase.
    ccexpyear = models.IntegerField(
        db_column="CCExpYear", blank=True, null=True
    )  # Field name made lowercase.
    ccname = models.CharField(
        db_column="CCName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccaddress = models.CharField(
        db_column="CCAddress",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccpostalcode = models.CharField(
        db_column="CCPostalCode",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    accountnumber = models.CharField(
        db_column="AccountNumber",
        max_length=99,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    comment = models.TextField(
        db_column="Comment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    popupnotes = models.BooleanField(
        db_column="PopupNotes"
    )  # Field name made lowercase.
    guidcurrency = models.CharField(
        db_column="GUIDCurrency", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    syncasguidcustomer = models.CharField(
        db_column="SyncAsGUIDCustomer", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    createdby = models.CharField(
        db_column="CreatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    createddate = models.DateTimeField(
        db_column="CreatedDate", blank=True, null=True
    )  # Field name made lowercase.
    updatedby = models.CharField(
        db_column="UpdatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    updateddate = models.DateTimeField(
        db_column="UpdatedDate", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tbcustomer"
        unique_together = (("guidparent", "custid"),)


class Tborders(models.Model):
    guidorder = models.CharField(db_column="GUIDOrder", primary_key=True, max_length=36)
    customer = models.ForeignKey(
        Tbcustomer, on_delete=models.PROTECT, db_column="GUIDCustomer"
    )
    ordernumber = models.CharField(
        db_column="OrderNumber",
        unique=True,
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    type = models.CharField(
        db_column="Type",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidbranch = models.CharField(
        db_column="GUIDBranch", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidcustomertype = models.CharField(
        db_column="GUIDCustomerType", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    orderdate = models.DateTimeField(
        db_column="OrderDate", blank=True, null=True
    )  # Field name made lowercase.
    entrydate = models.DateTimeField(
        db_column="EntryDate", blank=True, null=True
    )  # Field name made lowercase.
    enteredby = models.CharField(
        db_column="EnteredBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    orderstatus = models.CharField(
        db_column="OrderStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    statusdate = models.DateTimeField(
        db_column="StatusDate", blank=True, null=True
    )  # Field name made lowercase.
    statuschangedby = models.CharField(
        db_column="StatusChangedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    completed = models.BooleanField(db_column="Completed")  # Field name made lowercase.
    printed = models.BooleanField(db_column="Printed")  # Field name made lowercase.
    readytoprint = models.BooleanField(
        db_column="ReadyToPrint"
    )  # Field name made lowercase.
    pickticketprinted = models.BooleanField(
        db_column="PickTicketPrinted"
    )  # Field name made lowercase.
    pickticketreadytoprint = models.BooleanField(
        db_column="PickTicketReadyToPrint"
    )  # Field name made lowercase.
    shippingdocumentprinted = models.BooleanField(
        db_column="ShippingDocumentPrinted"
    )  # Field name made lowercase.
    shippingdocumentreadytoprint = models.BooleanField(
        db_column="ShippingDocumentReadyToPrint"
    )  # Field name made lowercase.
    creditapprovedby = models.CharField(
        db_column="CreditApprovedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    creditapprovaldate = models.DateTimeField(
        db_column="CreditApprovalDate", blank=True, null=True
    )  # Field name made lowercase.
    shipvia = models.CharField(
        db_column="ShipVia",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    fob = models.CharField(
        db_column="FOB",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )  # Field name made lowercase.
    shipmentpromiseddate = models.DateTimeField(
        db_column="ShipmentPromisedDate", blank=True, null=True
    )  # Field name made lowercase.
    dontshipbefore = models.DateTimeField(
        db_column="DontShipBefore", blank=True, null=True
    )  # Field name made lowercase.
    dontshipafter = models.DateTimeField(
        db_column="DontShipAfter", blank=True, null=True
    )  # Field name made lowercase.
    quoteddaystoship = models.IntegerField(
        db_column="QuotedDaysToShip", blank=True, null=True
    )  # Field name made lowercase.
    backordercriteria = models.CharField(
        db_column="BackorderCriteria",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    manualhold = models.BooleanField(
        db_column="ManualHold"
    )  # Field name made lowercase.
    holdreleasedby = models.CharField(
        db_column="HoldReleasedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    holdreleaseddate = models.DateTimeField(
        db_column="HoldReleasedDate", blank=True, null=True
    )  # Field name made lowercase.
    lastshipmentdate = models.DateTimeField(
        db_column="LastShipmentDate", blank=True, null=True
    )  # Field name made lowercase.

    soldtooverride = models.BooleanField(
        db_column="SoldToOverride"
    )  # Field name made lowercase.
    soldtoname = models.CharField(
        db_column="SoldToName",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtoaddress1 = models.CharField(
        db_column="SoldToAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtoaddress2 = models.CharField(
        db_column="SoldToAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtoaddress3 = models.CharField(
        db_column="SoldToAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtoaddress4 = models.CharField(
        db_column="SoldToAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtocity = models.CharField(
        db_column="SoldToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtostate = models.CharField(
        db_column="SoldToState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtozip = models.CharField(
        db_column="SoldToZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    soldtocountry = models.CharField(
        db_column="SoldToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidlocation = models.CharField(
        db_column="GUIDLocation", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    shiptooverride = models.BooleanField(
        db_column="ShipToOverride"
    )  # Field name made lowercase.
    shiptoattn = models.CharField(
        db_column="ShipToAttn",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptodescription = models.CharField(
        db_column="ShipToDescription",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptoaddress1 = models.CharField(
        db_column="ShipToAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptoaddress2 = models.CharField(
        db_column="ShipToAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptoaddress3 = models.CharField(
        db_column="ShipToAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptoaddress4 = models.CharField(
        db_column="ShipToAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptocity = models.CharField(
        db_column="ShipToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptostate = models.CharField(
        db_column="ShipToState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptozip = models.CharField(
        db_column="ShipToZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptocountry = models.CharField(
        db_column="ShipToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    po = models.CharField(
        db_column="PO",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    taxpct = models.DecimalField(
        db_column="TaxPct", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    frttaxpct = models.DecimalField(
        db_column="FrtTaxPct", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    taxpercenttext = models.CharField(
        db_column="TaxPercentText",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedsubtotal = models.DecimalField(
        db_column="SchedSubTotal",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    scheddiscountamount = models.DecimalField(
        db_column="SchedDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedsalestax = models.DecimalField(
        db_column="SchedSalesTax",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedshippingcharge = models.DecimalField(
        db_column="SchedShippingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedtotalamount = models.DecimalField(
        db_column="SchedTotalAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    subtotal = models.DecimalField(
        db_column="SubTotal", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    discounttype = models.CharField(
        db_column="DiscountType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    invoicediscountpct = models.DecimalField(
        db_column="InvoiceDiscountPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    discountamount = models.DecimalField(
        db_column="DiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    salestax = models.DecimalField(
        db_column="SalesTax", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    totalamount = models.DecimalField(
        db_column="TotalAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    reference = models.CharField(
        db_column="Reference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidterms = models.CharField(
        db_column="GUIDTerms", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    termsdescription = models.CharField(
        db_column="TermsDescription",
        max_length=31,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedtermsdiscountavailable = models.DecimalField(
        db_column="SchedTermsDiscountAvailable",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nextinvoicenumber = models.CharField(
        db_column="NextInvoiceNumber",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contractid = models.CharField(
        db_column="ContractID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    jobnumber = models.CharField(
        db_column="JobNumber",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    deliveredto = models.CharField(
        db_column="DeliveredTo",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    deliveredby = models.CharField(
        db_column="DeliveredBy",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    deliverydate = models.DateTimeField(
        db_column="DeliveryDate", blank=True, null=True
    )  # Field name made lowercase.
    deliverymiles = models.DecimalField(
        db_column="DeliveryMiles",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    numberofpackages = models.IntegerField(
        db_column="NumberOfPackages", blank=True, null=True
    )  # Field name made lowercase.
    packageweight = models.DecimalField(
        db_column="PackageWeight",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shippinginstructions = models.TextField(
        db_column="ShippingInstructions",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    specialinstructions = models.TextField(
        db_column="SpecialInstructions",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    comment = models.CharField(
        db_column="Comment",
        max_length=101,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lostbusinesscode = models.CharField(
        db_column="LostBusinessCode",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lostbusinesscomment = models.TextField(
        db_column="LostBusinessComment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    trackingnumber = models.CharField(
        db_column="TrackingNumber",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    reference2 = models.CharField(
        db_column="Reference2",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactname = models.CharField(
        db_column="ContactName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactphonenumber = models.CharField(
        db_column="ContactPhoneNumber",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactfax = models.CharField(
        db_column="ContactFax",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactemailaddress = models.CharField(
        db_column="ContactEMailAddress",
        max_length=253,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    pendingshippingcharges = models.DecimalField(
        db_column="PendingShippingCharges",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    amtpaid = models.DecimalField(
        db_column="AmtPaid", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    bankid = models.CharField(
        db_column="BankId",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccnumber = models.CharField(
        db_column="CCNumber",
        max_length=64,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccexpdate = models.CharField(
        db_column="CCExpDate",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccname = models.CharField(
        db_column="CCName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccaddress = models.CharField(
        db_column="CCAddress",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ccpostalcode = models.CharField(
        db_column="CCPostalCode",
        max_length=18,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    checkno = models.CharField(
        db_column="CheckNo",
        max_length=19,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    discamt = models.DecimalField(
        db_column="DiscAmt", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    methodofpayment = models.IntegerField(
        db_column="MethodOfPayment", blank=True, null=True
    )  # Field name made lowercase.
    guidpaymentmethod = models.CharField(
        db_column="GUIDPaymentMethod", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    readytoinvoice = models.BooleanField(
        db_column="ReadyToInvoice"
    )  # Field name made lowercase.
    invoicingerror = models.BooleanField(
        db_column="InvoicingError"
    )  # Field name made lowercase.
    invoicingerrormessage = models.TextField(
        db_column="InvoicingErrorMessage",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    carrier = models.CharField(
        db_column="Carrier",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    carrierservice = models.CharField(
        db_column="CarrierService",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nextshipmentnumber = models.SmallIntegerField(
        db_column="NextShipmentNumber", blank=True, null=True
    )  # Field name made lowercase.
    marketingcode = models.CharField(
        db_column="MarketingCode",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidsalesperson = models.CharField(
        db_column="GUIDSalesperson", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidtaxcategory = models.CharField(
        db_column="GUIDTaxCategory", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidclass = models.CharField(
        db_column="GUIDClass", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidorderworkflowstatus = models.CharField(
        db_column="GUIDOrderWorkFlowStatus", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    beingpickedby = models.CharField(
        db_column="BeingPickedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    workflowstatuschangedby = models.CharField(
        db_column="WorkFlowStatusChangedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    workflowstatusdate = models.DateTimeField(
        db_column="WorkFlowStatusDate", blank=True, null=True
    )  # Field name made lowercase.
    origintype = models.CharField(
        db_column="OriginType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    originid = models.CharField(
        db_column="OriginID",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidroute = models.CharField(
        db_column="GUIDRoute", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    stopnumber = models.DecimalField(
        db_column="StopNumber", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    taxincluded = models.BooleanField(
        db_column="TaxIncluded"
    )  # Field name made lowercase.
    guidtemplate = models.CharField(
        db_column="GUIDTemplate", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    webordernumber = models.CharField(
        db_column="WebOrderNumber",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    weborderid = models.CharField(
        db_column="WebOrderID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    updatedby = models.CharField(
        db_column="UpdatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    updateddate = models.DateTimeField(
        db_column="UpdatedDate", blank=True, null=True
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=19, decimal_places=7
    )  # Field name made lowercase.
    guidrelatedorder = models.CharField(
        db_column="GUIDRelatedOrder", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    shipworkstationexportdate = models.DateTimeField(
        db_column="ShipWorkstationExportDate", blank=True, null=True
    )  # Field name made lowercase.
    webcustomerid = models.CharField(
        db_column="WebCustomerID",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    redactionstatus = models.CharField(
        db_column="RedactionStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    invoiceformatguid = models.CharField(
        db_column="InvoiceFormatGUID", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tborders"


class Tborderdetail(models.Model):
    guidorderdetail = models.CharField(
        db_column="GUIDOrderDetail", primary_key=True, max_length=36
    )  # Field name made lowercase.
    guidorder = models.CharField(
        db_column="GUIDOrder", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    linenumber = models.IntegerField(
        db_column="LineNumber", blank=True, null=True
    )  # Field name made lowercase.
    sublinenumber = models.IntegerField(
        db_column="SubLineNumber"
    )  # Field name made lowercase.
    componentlevel = models.IntegerField(
        db_column="ComponentLevel"
    )  # Field name made lowercase.
    linetype = models.CharField(
        db_column="LineType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidproduct = models.CharField(
        db_column="GUIDProduct", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    productid = models.CharField(
        db_column="ProductID",
        max_length=159,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidsubstituteforproduct = models.CharField(
        db_column="GUIDSubstituteForProduct", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    qtyordered = models.DecimalField(
        db_column="QtyOrdered", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    qtyshipped = models.DecimalField(
        db_column="QtyShipped", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    qtypicked = models.DecimalField(
        db_column="QtyPicked", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    qtyscheduled = models.DecimalField(
        db_column="QtyScheduled", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    qtyinvoiced = models.DecimalField(
        db_column="QtyInvoiced", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    qtybackordered = models.DecimalField(
        db_column="QtyBackordered",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    completed = models.BooleanField(db_column="Completed")  # Field name made lowercase.
    linecancelled = models.BooleanField(
        db_column="LineCancelled"
    )  # Field name made lowercase.
    unit = models.CharField(
        db_column="Unit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    displayunit = models.CharField(
        db_column="DisplayUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    displayunitfactor = models.DecimalField(
        db_column="DisplayUnitFactor",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    pricecode = models.CharField(
        db_column="PriceCode",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    price = models.DecimalField(
        db_column="Price", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    displayprice = models.DecimalField(
        db_column="DisplayPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    linetaxprice = models.DecimalField(
        db_column="LineTaxPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    priceunit = models.CharField(
        db_column="PriceUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    priceunitfactor = models.DecimalField(
        db_column="PriceUnitFactor",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    priceunitfactortype = models.CharField(
        db_column="PriceUnitFactorType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    producttaxid = models.CharField(
        db_column="ProductTaxID",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    miscchargetype = models.CharField(
        db_column="MiscChargeType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    freight = models.BooleanField(db_column="Freight")  # Field name made lowercase.
    producttaxpct = models.DecimalField(
        db_column="ProductTaxPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    linediscountpct = models.DecimalField(
        db_column="LineDiscountPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    displayamount = models.DecimalField(
        db_column="DisplayAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    invoicediscountamount = models.DecimalField(
        db_column="InvoiceDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    linetaxamount = models.DecimalField(
        db_column="LineTaxAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedamount = models.DecimalField(
        db_column="SchedAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    schedinvoicediscountamount = models.DecimalField(
        db_column="SchedInvoiceDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    schedlinetaxamount = models.DecimalField(
        db_column="SchedLineTaxAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    discountable = models.BooleanField(
        db_column="Discountable"
    )  # Field name made lowercase.
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidproductclass = models.CharField(
        db_column="GUIDProductClass", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    length = models.DecimalField(
        db_column="Length", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    weight = models.DecimalField(
        db_column="Weight", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    variablelength = models.BooleanField(
        db_column="VariableLength"
    )  # Field name made lowercase.
    variableweight = models.BooleanField(
        db_column="VariableWeight"
    )  # Field name made lowercase.
    specification = models.CharField(
        db_column="Specification",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    specialinstructions = models.TextField(
        db_column="SpecialInstructions",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    invoicecomment = models.TextField(
        db_column="InvoiceComment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    inventorycontroltype = models.CharField(
        db_column="InventoryControlType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    qtylotserial = models.DecimalField(
        db_column="QtyLotSerial", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    salescategory = models.CharField(
        db_column="SalesCategory",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    poprice = models.DecimalField(
        db_column="POPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    createpo = models.BooleanField(db_column="CreatePO")  # Field name made lowercase.
    componentquantity = models.DecimalField(
        db_column="ComponentQuantity",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidparentorderdetail = models.CharField(
        db_column="GUIDParentOrderDetail", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidvendor = models.CharField(
        db_column="GUIDVendor", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidpodetail = models.CharField(
        db_column="GUIDPODetail", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidclass = models.CharField(
        db_column="GUIDClass", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    guidissue = models.CharField(
        db_column="GUIDIssue", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    reference = models.CharField(
        db_column="Reference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    activitydate = models.DateTimeField(
        db_column="ActivityDate", blank=True, null=True
    )  # Field name made lowercase.
    guidemployee = models.CharField(
        db_column="GUIDEmployee", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    billingtype = models.CharField(
        db_column="BillingType",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    tobebilled = models.BooleanField(
        db_column="ToBeBilled"
    )  # Field name made lowercase.
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    exported940 = models.BooleanField(
        db_column="Exported940"
    )  # Field name made lowercase.
    exported940date = models.DateTimeField(
        db_column="Exported940Date", blank=True, null=True
    )  # Field name made lowercase.
    weborderlineid = models.CharField(
        db_column="WebOrderLineID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tborderdetail"


class Volusionproducts(models.Model):
    productcode = models.CharField(
        db_column="ProductCode",
        primary_key=True,
        max_length=150,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    productname = models.CharField(
        db_column="ProductName",
        max_length=350,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productdescription = models.TextField(
        db_column="ProductDescription",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    extinfo = models.TextField(
        db_column="ExtInfo",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    techspecs = models.TextField(
        db_column="TechSpecs",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productprice = models.DecimalField(
        db_column="ProductPrice", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    lastmodby = models.CharField(
        db_column="LastModBy",
        max_length=10,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lastmodified = models.DateTimeField(
        db_column="LastModified", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "volusionproducts"


"""    _                   
__   _(_) _____      _____ 
\ \ / / |/ _ \ \ /\ / / __|
 \ V /| |  __/\ V  V /\__ \
  \_/ |_|\___| \_/\_/ |___/
                           
"""


class Productwarehousesummary(models.Model):
    guidproductwarehouse = models.CharField(
        db_column="GUIDProductWarehouse", max_length=36
    )
    guidproduct = models.CharField(db_column="GUIDProduct", max_length=36)
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

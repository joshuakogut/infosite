from django.db import models
from django.db.models import Q
from django.utils import timezone
import humanfriendly as hf
from portal import Logger

logger = Logger("portal.models")


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


class Tbcustomer(models.Model):
    guidcustomer = models.CharField(
        db_column="GUIDCustomer", primary_key=True, max_length=36
    )
    custlistid = models.CharField(
        db_column="CustListID",
        unique=True,
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    custid = models.CharField(
        db_column="CustId", max_length=500, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    guidparent = models.CharField(
        db_column="GUIDParent", max_length=36, blank=True, null=True
    )
    method = models.IntegerField(db_column="Method", blank=True, null=True)
    guidcustomertype = models.CharField(
        db_column="GUIDCustomerType", max_length=36, blank=True, null=True
    )
    companyname = models.CharField(
        db_column="CompanyName",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    name = models.CharField(
        db_column="Name",
        max_length=500,
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
    address = models.CharField(
        db_column="Address",
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
    phone = models.CharField(
        db_column="Phone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    phonedesc = models.CharField(
        db_column="PhoneDesc",
        max_length=41,
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
    faxdesc = models.CharField(
        db_column="FaxDesc",
        max_length=41,
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
    emaildesc = models.CharField(
        db_column="EmailDesc",
        max_length=41,
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
    altphonedesc = models.CharField(
        db_column="AltPhoneDesc",
        max_length=41,
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
    mobiledesc = models.CharField(
        db_column="MobileDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pager = models.CharField(
        db_column="Pager",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pagerdesc = models.CharField(
        db_column="PagerDesc",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidsalesperson = models.CharField(
        db_column="GUIDSalesperson", max_length=36, blank=True, null=True
    )
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )
    statesalestaxid = models.CharField(
        db_column="StateSalesTaxId",
        max_length=16,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    taxexemptionreasonid = models.IntegerField(
        db_column="TaxExemptionReasonID", blank=True, null=True
    )
    taxincluded = models.BooleanField(db_column="TaxIncluded")
    guidterms = models.CharField(
        db_column="GUIDTerms", max_length=36, blank=True, null=True
    )
    locationid = models.CharField(
        db_column="LocationId",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    creditlimit = models.DecimalField(
        db_column="CreditLimit", max_digits=19, decimal_places=4, blank=True, null=True
    )
    credithold = models.BooleanField(db_column="CreditHold")
    preferredpaymentmethod = models.CharField(
        db_column="PreferredPaymentMethod", max_length=36, blank=True, null=True
    )
    status = models.BooleanField(db_column="Status", blank=True, null=True)
    ccnumber = models.CharField(
        db_column="CCNumber",
        max_length=64,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccdisplaynumber = models.CharField(
        db_column="CCDisplayNumber",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccexpmonth = models.IntegerField(db_column="CCExpMonth", blank=True, null=True)
    ccexpyear = models.IntegerField(db_column="CCExpYear", blank=True, null=True)
    ccname = models.CharField(
        db_column="CCName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccaddress = models.CharField(
        db_column="CCAddress",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccpostalcode = models.CharField(
        db_column="CCPostalCode",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    accountnumber = models.CharField(
        db_column="AccountNumber",
        max_length=99,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    comment = models.TextField(
        db_column="Comment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    popupnotes = models.BooleanField(db_column="PopupNotes")
    guidcurrency = models.CharField(
        db_column="GUIDCurrency", max_length=36, blank=True, null=True
    )
    syncasguidcustomer = models.CharField(
        db_column="SyncAsGUIDCustomer", max_length=36, blank=True, null=True
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

    class Meta:
        managed = False
        db_table = "tbcustomer"
        unique_together = (("guidparent", "custid"),)

from portal.models import *


class Tborders(models.Model):
    guidorder = models.CharField(db_column="GUIDOrder", primary_key=True, max_length=36)

    workflowstatus = models.ForeignKey(
        "Tborderworkflowstatus",
        on_delete=models.PROTECT,
        db_column="GUIDOrderWorkFlowStatus",
        related_name="orders",
    )
    customer = models.ForeignKey(
        Tbcustomer, on_delete=models.PROTECT, db_column="GUIDCustomer"
    )
    ordernumber = models.CharField(
        db_column="OrderNumber",
        unique=True,
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    type = models.CharField(
        db_column="Type",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidbranch = models.CharField(
        db_column="GUIDBranch", max_length=36, blank=True, null=True
    )
    guidcustomertype = models.CharField(
        db_column="GUIDCustomerType", max_length=36, blank=True, null=True
    )
    orderdate = models.DateTimeField(db_column="OrderDate", blank=True, null=True)
    entrydate = models.DateTimeField(db_column="EntryDate", blank=True, null=True)
    enteredby = models.CharField(
        db_column="EnteredBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    orderstatus = models.CharField(
        db_column="OrderStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    statusdate = models.DateTimeField(db_column="StatusDate", blank=True, null=True)
    statuschangedby = models.CharField(
        db_column="StatusChangedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    completed = models.BooleanField(db_column="Completed")
    printed = models.BooleanField(db_column="Printed")
    readytoprint = models.BooleanField(db_column="ReadyToPrint")
    pickticketprinted = models.BooleanField(db_column="PickTicketPrinted")
    pickticketreadytoprint = models.BooleanField(db_column="PickTicketReadyToPrint")
    shippingdocumentprinted = models.BooleanField(db_column="ShippingDocumentPrinted")
    shippingdocumentreadytoprint = models.BooleanField(
        db_column="ShippingDocumentReadyToPrint"
    )
    creditapprovedby = models.CharField(
        db_column="CreditApprovedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    creditapprovaldate = models.DateTimeField(
        db_column="CreditApprovalDate", blank=True, null=True
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
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )
    shipmentpromiseddate = models.DateTimeField(
        db_column="ShipmentPromisedDate", blank=True, null=True
    )
    dontshipbefore = models.DateTimeField(
        db_column="DontShipBefore", blank=True, null=True
    )
    dontshipafter = models.DateTimeField(
        db_column="DontShipAfter", blank=True, null=True
    )
    quoteddaystoship = models.IntegerField(
        db_column="QuotedDaysToShip", blank=True, null=True
    )
    backordercriteria = models.CharField(
        db_column="BackorderCriteria",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    manualhold = models.BooleanField(db_column="ManualHold")
    holdreleasedby = models.CharField(
        db_column="HoldReleasedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    holdreleaseddate = models.DateTimeField(
        db_column="HoldReleasedDate", blank=True, null=True
    )
    lastshipmentdate = models.DateTimeField(
        db_column="LastShipmentDate", blank=True, null=True
    )

    soldtooverride = models.BooleanField(db_column="SoldToOverride")
    soldtoname = models.CharField(
        db_column="SoldToName",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtoaddress1 = models.CharField(
        db_column="SoldToAddress1",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtoaddress2 = models.CharField(
        db_column="SoldToAddress2",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtoaddress3 = models.CharField(
        db_column="SoldToAddress3",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtoaddress4 = models.CharField(
        db_column="SoldToAddress4",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtocity = models.CharField(
        db_column="SoldToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtostate = models.CharField(
        db_column="SoldToState",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtozip = models.CharField(
        db_column="SoldToZip",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    soldtocountry = models.CharField(
        db_column="SoldToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidlocation = models.CharField(
        db_column="GUIDLocation", max_length=36, blank=True, null=True
    )
    shiptooverride = models.BooleanField(db_column="ShipToOverride")
    shiptoattn = models.CharField(
        db_column="ShipToAttn",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptodescription = models.CharField(
        db_column="ShipToDescription",
        max_length=30,
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
    shiptocity = models.CharField(
        db_column="ShipToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
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
    shiptocountry = models.CharField(
        db_column="ShipToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    po = models.CharField(
        db_column="PO",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )
    taxpct = models.DecimalField(
        db_column="TaxPct", max_digits=19, decimal_places=7, blank=True, null=True
    )
    frttaxpct = models.DecimalField(
        db_column="FrtTaxPct", max_digits=19, decimal_places=7, blank=True, null=True
    )
    taxpercenttext = models.CharField(
        db_column="TaxPercentText",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    schedsubtotal = models.DecimalField(
        db_column="SchedSubTotal",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    scheddiscountamount = models.DecimalField(
        db_column="SchedDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    schedsalestax = models.DecimalField(
        db_column="SchedSalesTax",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    schedshippingcharge = models.DecimalField(
        db_column="SchedShippingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    schedtotalamount = models.DecimalField(
        db_column="SchedTotalAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    subtotal = models.DecimalField(
        db_column="SubTotal", max_digits=19, decimal_places=4, blank=True, null=True
    )
    discounttype = models.CharField(
        db_column="DiscountType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    invoicediscountpct = models.DecimalField(
        db_column="InvoiceDiscountPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    discountamount = models.DecimalField(
        db_column="DiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    salestax = models.DecimalField(
        db_column="SalesTax", max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalamount = models.DecimalField(
        db_column="TotalAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    reference = models.CharField(
        db_column="Reference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidterms = models.CharField(
        db_column="GUIDTerms", max_length=36, blank=True, null=True
    )
    termsdescription = models.CharField(
        db_column="TermsDescription",
        max_length=31,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    schedtermsdiscountavailable = models.DecimalField(
        db_column="SchedTermsDiscountAvailable",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    nextinvoicenumber = models.CharField(
        db_column="NextInvoiceNumber",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contractid = models.CharField(
        db_column="ContractID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    jobnumber = models.CharField(
        db_column="JobNumber",
        max_length=20,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    deliveredto = models.CharField(
        db_column="DeliveredTo",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    deliveredby = models.CharField(
        db_column="DeliveredBy",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    deliverydate = models.DateTimeField(db_column="DeliveryDate", blank=True, null=True)
    deliverymiles = models.DecimalField(
        db_column="DeliveryMiles",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    numberofpackages = models.IntegerField(
        db_column="NumberOfPackages", blank=True, null=True
    )
    packageweight = models.DecimalField(
        db_column="PackageWeight",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    shippinginstructions = models.TextField(
        db_column="ShippingInstructions",
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
    comment = models.CharField(
        db_column="Comment",
        max_length=101,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lostbusinesscode = models.CharField(
        db_column="LostBusinessCode",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lostbusinesscomment = models.TextField(
        db_column="LostBusinessComment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    trackingnumber = models.CharField(
        db_column="TrackingNumber",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    reference2 = models.CharField(
        db_column="Reference2",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactname = models.CharField(
        db_column="ContactName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactphonenumber = models.CharField(
        db_column="ContactPhoneNumber",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactfax = models.CharField(
        db_column="ContactFax",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactemailaddress = models.CharField(
        db_column="ContactEMailAddress",
        max_length=253,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    pendingshippingcharges = models.DecimalField(
        db_column="PendingShippingCharges",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    amtpaid = models.DecimalField(
        db_column="AmtPaid", max_digits=19, decimal_places=4, blank=True, null=True
    )
    bankid = models.CharField(
        db_column="BankId",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccnumber = models.CharField(
        db_column="CCNumber",
        max_length=64,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    ccexpdate = models.CharField(
        db_column="CCExpDate",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
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
        max_length=18,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    checkno = models.CharField(
        db_column="CheckNo",
        max_length=19,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    discamt = models.DecimalField(
        db_column="DiscAmt", max_digits=19, decimal_places=4, blank=True, null=True
    )
    methodofpayment = models.IntegerField(
        db_column="MethodOfPayment", blank=True, null=True
    )
    guidpaymentmethod = models.CharField(
        db_column="GUIDPaymentMethod", max_length=36, blank=True, null=True
    )
    readytoinvoice = models.BooleanField(db_column="ReadyToInvoice")
    invoicingerror = models.BooleanField(db_column="InvoicingError")
    invoicingerrormessage = models.TextField(
        db_column="InvoicingErrorMessage",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrier = models.CharField(
        db_column="Carrier",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrierservice = models.CharField(
        db_column="CarrierService",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    nextshipmentnumber = models.SmallIntegerField(
        db_column="NextShipmentNumber", blank=True, null=True
    )
    marketingcode = models.CharField(
        db_column="MarketingCode",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidsalesperson = models.CharField(
        db_column="GUIDSalesperson", max_length=36, blank=True, null=True
    )
    guidtaxcategory = models.CharField(
        db_column="GUIDTaxCategory", max_length=36, blank=True, null=True
    )
    guidclass = models.CharField(
        db_column="GUIDClass", max_length=36, blank=True, null=True
    )

    beingpickedby = models.CharField(
        db_column="BeingPickedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    workflowstatuschangedby = models.CharField(
        db_column="WorkFlowStatusChangedBy",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    workflowstatusdate = models.DateTimeField(
        db_column="WorkFlowStatusDate", blank=True, null=True
    )
    origintype = models.CharField(
        db_column="OriginType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    originid = models.CharField(
        db_column="OriginID",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidroute = models.CharField(
        db_column="GUIDRoute", max_length=36, blank=True, null=True
    )
    stopnumber = models.DecimalField(
        db_column="StopNumber", max_digits=19, decimal_places=7, blank=True, null=True
    )
    taxincluded = models.BooleanField(db_column="TaxIncluded")
    guidtemplate = models.CharField(
        db_column="GUIDTemplate", max_length=36, blank=True, null=True
    )
    webordernumber = models.CharField(
        db_column="WebOrderNumber",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    weborderid = models.CharField(
        db_column="WebOrderID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    updatedby = models.CharField(
        db_column="UpdatedBy",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    updateddate = models.DateTimeField(db_column="UpdatedDate", blank=True, null=True)
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=19, decimal_places=7
    )
    guidrelatedorder = models.CharField(
        db_column="GUIDRelatedOrder", max_length=36, blank=True, null=True
    )
    shipworkstationexportdate = models.DateTimeField(
        db_column="ShipWorkstationExportDate", blank=True, null=True
    )
    webcustomerid = models.CharField(
        db_column="WebCustomerID",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    redactionstatus = models.CharField(
        db_column="RedactionStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    invoiceformatguid = models.CharField(
        db_column="InvoiceFormatGUID", max_length=36, blank=True, null=True
    )

    shipments = models.ManyToManyField("Tbshipment", through="Tbshipmentorder")

    class Meta:
        managed = False
        db_table = "tborders"


class Tborderdetail(models.Model):
    guidorderdetail = models.CharField(
        db_column="GUIDOrderDetail", primary_key=True, max_length=36
    )
    guidorder = models.ForeignKey(
        "Tborders",
        on_delete=models.DO_NOTHING,
        db_column="GUIDOrder",
        related_name="details",
        blank=True,
        null=True,
    )
    linenumber = models.IntegerField(db_column="LineNumber", blank=True, null=True)
    sublinenumber = models.IntegerField(db_column="SubLineNumber")
    componentlevel = models.IntegerField(db_column="ComponentLevel")
    linetype = models.CharField(
        db_column="LineType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidproduct = models.ForeignKey(
        "product.Tbproduct",
        on_delete=models.DO_NOTHING,
        db_column="GUIDProduct",
        related_name="orderdetails",
        blank=True,
        null=True,
    )
    productid = models.CharField(
        db_column="ProductID",
        max_length=159,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36, blank=True, null=True
    )
    description = models.TextField(
        db_column="Description",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    guidsubstituteforproduct = models.CharField(
        db_column="GUIDSubstituteForProduct", max_length=36, blank=True, null=True
    )
    qtyordered = models.DecimalField(
        db_column="QtyOrdered", max_digits=19, decimal_places=7, blank=True, null=True
    )
    qtyshipped = models.DecimalField(
        db_column="QtyShipped", max_digits=19, decimal_places=7, blank=True, null=True
    )
    qtypicked = models.DecimalField(
        db_column="QtyPicked", max_digits=19, decimal_places=7, blank=True, null=True
    )
    qtyscheduled = models.DecimalField(
        db_column="QtyScheduled", max_digits=19, decimal_places=7, blank=True, null=True
    )
    qtyinvoiced = models.DecimalField(
        db_column="QtyInvoiced", max_digits=19, decimal_places=7, blank=True, null=True
    )
    qtybackordered = models.DecimalField(
        db_column="QtyBackordered",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    completed = models.BooleanField(db_column="Completed")
    linecancelled = models.BooleanField(db_column="LineCancelled")
    unit = models.CharField(
        db_column="Unit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
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
    pricecode = models.CharField(
        db_column="PriceCode",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        db_column="Price", max_digits=19, decimal_places=7, blank=True, null=True
    )
    displayprice = models.DecimalField(
        db_column="DisplayPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    linetaxprice = models.DecimalField(
        db_column="LineTaxPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    priceunit = models.CharField(
        db_column="PriceUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    priceunitfactor = models.DecimalField(
        db_column="PriceUnitFactor",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    priceunitfactortype = models.CharField(
        db_column="PriceUnitFactorType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    producttaxid = models.CharField(
        db_column="ProductTaxID",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    miscchargetype = models.CharField(
        db_column="MiscChargeType",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    freight = models.BooleanField(db_column="Freight")
    producttaxpct = models.DecimalField(
        db_column="ProductTaxPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    linediscountpct = models.DecimalField(
        db_column="LineDiscountPct",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        db_column="Amount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    displayamount = models.DecimalField(
        db_column="DisplayAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    invoicediscountamount = models.DecimalField(
        db_column="InvoiceDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    linetaxamount = models.DecimalField(
        db_column="LineTaxAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    schedamount = models.DecimalField(
        db_column="SchedAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    schedinvoicediscountamount = models.DecimalField(
        db_column="SchedInvoiceDiscountAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    schedlinetaxamount = models.DecimalField(
        db_column="SchedLineTaxAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    discountable = models.BooleanField(db_column="Discountable")
    guidtaxcode = models.CharField(
        db_column="GUIDTaxCode", max_length=36, blank=True, null=True
    )
    guidproductclass = models.CharField(
        db_column="GUIDProductClass", max_length=36, blank=True, null=True
    )
    length = models.DecimalField(
        db_column="Length", max_digits=19, decimal_places=7, blank=True, null=True
    )
    weight = models.DecimalField(
        db_column="Weight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    variablelength = models.BooleanField(db_column="VariableLength")
    variableweight = models.BooleanField(db_column="VariableWeight")
    specification = models.CharField(
        db_column="Specification",
        max_length=80,
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
    invoicecomment = models.TextField(
        db_column="InvoiceComment",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    note = models.TextField(
        db_column="Note",
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
    qtylotserial = models.DecimalField(
        db_column="QtyLotSerial", max_digits=19, decimal_places=7, blank=True, null=True
    )
    salescategory = models.CharField(
        db_column="SalesCategory",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    poprice = models.DecimalField(
        db_column="POPrice", max_digits=19, decimal_places=7, blank=True, null=True
    )
    createpo = models.BooleanField(db_column="CreatePO")
    componentquantity = models.DecimalField(
        db_column="ComponentQuantity",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )
    guidparentorderdetail = models.CharField(
        db_column="GUIDParentOrderDetail", max_length=36, blank=True, null=True
    )
    guidvendor = models.CharField(
        db_column="GUIDVendor", max_length=36, blank=True, null=True
    )
    guidpodetail = models.CharField(
        db_column="GUIDPODetail", max_length=36, blank=True, null=True
    )
    guidclass = models.CharField(
        db_column="GUIDClass", max_length=36, blank=True, null=True
    )
    guidissue = models.CharField(
        db_column="GUIDIssue", max_length=36, blank=True, null=True
    )
    reference = models.CharField(
        db_column="Reference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    activitydate = models.DateTimeField(db_column="ActivityDate", blank=True, null=True)
    guidemployee = models.CharField(
        db_column="GUIDEmployee", max_length=36, blank=True, null=True
    )
    billingtype = models.CharField(
        db_column="BillingType",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    tobebilled = models.BooleanField(db_column="ToBeBilled")
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", max_length=36, blank=True, null=True
    )
    exported940 = models.BooleanField(db_column="Exported940")
    exported940date = models.DateTimeField(
        db_column="Exported940Date", blank=True, null=True
    )
    weborderlineid = models.CharField(
        db_column="WebOrderLineID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "tborderdetail"


class Tbshipmentorder(models.Model):
    guidshipmentorder = models.CharField(
        db_column="GUIDShipmentOrder", primary_key=True, max_length=36
    )
    shipment = models.ForeignKey(
        "Tbshipment", on_delete=models.PROTECT, db_column="GUIDShipment"
    )

    order = models.ForeignKey(
        "Tborders", on_delete=models.PROTECT, db_column="GUIDOrder"
    )

    class Meta:
        managed = False
        db_table = "tbshipmentorder"


class Tbshipment(models.Model):
    guidshipment = models.CharField(
        db_column="GUIDShipment", primary_key=True, max_length=36
    )

    customer = models.ForeignKey(
        Tbcustomer, on_delete=models.PROTECT, db_column="GUIDCustomer"
    )

    shipmentnumber = models.CharField(
        db_column="ShipmentNumber",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipmentstatus = models.CharField(
        db_column="ShipmentStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipmentdate = models.DateTimeField(db_column="ShipmentDate", blank=True, null=True)
    scheduleddeliverydate = models.DateTimeField(
        db_column="ScheduledDeliveryDate", blank=True, null=True
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
    readytoprint = models.BooleanField(db_column="ReadyToPrint")
    printed = models.BooleanField(db_column="Printed")
    exported856 = models.BooleanField(db_column="Exported856")
    exported856date = models.DateTimeField(
        db_column="Exported856Date", blank=True, null=True
    )
    packagingcode = models.CharField(
        db_column="PackagingCode",
        max_length=12,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    numberofpieces = models.IntegerField(
        db_column="NumberOfPieces", blank=True, null=True
    )
    grossweight = models.DecimalField(
        db_column="GrossWeight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    grossweightunit = models.CharField(
        db_column="GrossWeightUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrier = models.CharField(
        db_column="Carrier",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrierservice = models.CharField(
        db_column="CarrierService",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrierreference = models.CharField(
        db_column="CarrierReference",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    transportationtype = models.CharField(
        db_column="TransportationType",
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    routing = models.CharField(
        db_column="Routing",
        max_length=35,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    billoflading = models.CharField(
        db_column="BillOfLading",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptoattn = models.CharField(
        db_column="ShipToAttn",
        max_length=50,
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
    shiptocity = models.CharField(
        db_column="ShipToCity",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
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
    shiptocountry = models.CharField(
        db_column="ShipToCountry",
        max_length=255,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shiptolocation = models.CharField(
        db_column="ShipToLocation",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactname = models.CharField(
        db_column="ContactName",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    contactphonenumber = models.CharField(
        db_column="ContactPhoneNumber",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    codamount = models.DecimalField(
        db_column="CODAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    declaredvalue = models.DecimalField(
        db_column="DeclaredValue",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    shippingcharge = models.DecimalField(
        db_column="ShippingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    handlingcharge = models.DecimalField(
        db_column="HandlingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    freightcollect = models.BooleanField(db_column="FreightCollect")
    insured = models.BooleanField(db_column="Insured")
    guidinvoice = models.CharField(
        db_column="GUIDInvoice", max_length=36, blank=True, null=True
    )
    guidpartner = models.CharField(
        db_column="GUIDPartner", max_length=36, blank=True, null=True
    )
    warehouseshipmentnumber = models.CharField(
        db_column="WarehouseShipmentNumber",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    webshipmentid = models.CharField(
        db_column="WebShipmentID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    websyncdate = models.DateTimeField(db_column="WebSyncDate", blank=True, null=True)
    shipwsguidtemplate = models.CharField(
        db_column="ShipWSGUIDTemplate", max_length=36, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "tbshipment"


class Tbshipmentpack(models.Model):
    guidshipmentpack = models.CharField(
        db_column="GUIDShipmentPack", primary_key=True, max_length=36
    )

    shipment = models.ForeignKey(
        Tbshipment,
        on_delete=models.PROTECT,
        db_column="GUIDShipment",
        related_name="packages",
    )

    packnumber = models.IntegerField(db_column="PackNumber", blank=True, null=True)
    qtyshipped = models.DecimalField(
        db_column="QtyShipped", max_digits=19, decimal_places=7, blank=True, null=True
    )
    weight = models.DecimalField(
        db_column="Weight", max_digits=19, decimal_places=7, blank=True, null=True
    )
    weightunit = models.CharField(
        db_column="WeightUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    outerpack = models.IntegerField(db_column="OuterPack", blank=True, null=True)
    innerpack = models.IntegerField(db_column="InnerPack", blank=True, null=True)
    packagingcode = models.CharField(
        db_column="PackagingCode",
        max_length=12,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    carrierpackageid = models.CharField(
        db_column="CarrierPackageID",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    packageid = models.CharField(
        db_column="PackageID",
        max_length=48,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    storelocation = models.CharField(
        db_column="StoreLocation",
        max_length=41,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    voided = models.BooleanField(db_column="Voided")
    voiddate = models.DateTimeField(db_column="VoidDate", blank=True, null=True)
    notbillable = models.BooleanField(db_column="NotBillable")
    comment = models.CharField(
        db_column="Comment",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    codamount = models.DecimalField(
        db_column="CODAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    declaredvalue = models.DecimalField(
        db_column="DeclaredValue",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    shippingcharge = models.DecimalField(
        db_column="ShippingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    handlingcharge = models.DecimalField(
        db_column="HandlingCharge",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    shipmentdate = models.DateTimeField(db_column="ShipmentDate", blank=True, null=True)
    webpackageid = models.CharField(
        db_column="WebPackageID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    shipwspackageid = models.CharField(
        db_column="ShipWSPackageID",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "tbshipmentpack"


class Tborderworkflowstatus(models.Model):
    guidorderworkflowstatus = models.CharField(
        db_column="GUIDOrderWorkFlowStatus", primary_key=True, max_length=36
    )  # Field name made lowercase.
    description = models.CharField(
        db_column="Description",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    abbreviation = models.CharField(
        db_column="Abbreviation",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    workflowstatus = models.CharField(
        db_column="WorkFlowStatus",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tborderworkflowstatus"

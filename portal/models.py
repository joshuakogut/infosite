# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Productwarehousesummary(models.Model):
    guidproductwarehouse = models.CharField(db_column='GUIDProductWarehouse', max_length=36)  # Field name made lowercase.
    guidproduct = models.CharField(db_column='GUIDProduct', max_length=36)  # Field name made lowercase.
    guidwarehouse = models.CharField(db_column='GUIDWarehouse', max_length=36, blank=True, null=True)  # Field name made lowercase.
    warehouse = models.CharField(db_column='Warehouse', max_length=6, blank=True, null=True)  # Field name made lowercase.
    warehousedescription = models.CharField(db_column='WarehouseDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=159)  # Field name made lowercase.
    qtyreserved = models.DecimalField(db_column='QtyReserved', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    guidwhlocation = models.CharField(db_column='GUIDWHLocation', max_length=36, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=80, blank=True, null=True)  # Field name made lowercase.
    primarylocationstockinglevel = models.DecimalField(db_column='PrimaryLocationStockingLevel', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    lastcost = models.DecimalField(db_column='LastCost', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    mgmtcost = models.DecimalField(db_column='MgmtCost', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    standardcost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    reorderpoint = models.DecimalField(db_column='ReorderPoint', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    stockinglevel = models.DecimalField(db_column='StockingLevel', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtytoreorder = models.DecimalField(db_column='QtyToReorder', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    lastcountdate = models.DateTimeField(db_column='LastCountDate', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.DecimalField(db_column='QtyOnHand', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    onhandvalue = models.DecimalField(db_column='OnHandValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    avgcost = models.DecimalField(db_column='AvgCost', max_digits=38, decimal_places=16, blank=True, null=True)  # Field name made lowercase.
    quantityonpo = models.DecimalField(db_column='QuantityOnPO', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    quantityonreturn = models.DecimalField(db_column='QuantityOnReturn', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    quantityonorder = models.DecimalField(db_column='QuantityOnOrder', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    amountonorder = models.DecimalField(db_column='AmountOnOrder', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtyordered = models.DecimalField(db_column='QtyOrdered', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtybooked = models.DecimalField(db_column='QtyBooked', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtyscheduled = models.DecimalField(db_column='QtyScheduled', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtybackordered = models.DecimalField(db_column='QtyBackordered', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtyspecialorder = models.DecimalField(db_column='QtySpecialOrder', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    unpostedcomponentquantity = models.DecimalField(db_column='UnpostedComponentQuantity', max_digits=38, decimal_places=13, blank=True, null=True)  # Field name made lowercase.
    unpostedassemblyquantity = models.DecimalField(db_column='UnpostedAssemblyQuantity', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    unpostedtransferquantity = models.DecimalField(db_column='UnpostedTransferQuantity', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    qtyorderedamount = models.DecimalField(db_column='QtyOrderedAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtyschedamount = models.DecimalField(db_column='QtySchedAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allocated = models.DecimalField(db_column='Allocated', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    available = models.DecimalField(db_column='Available', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    lasttransactiondate = models.DateTimeField(db_column='LastTransactionDate', blank=True, null=True)  # Field name made lowercase.
    qtyrequired = models.DecimalField(db_column='QtyRequired', max_digits=38, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    stdcost = models.DecimalField(db_column='StdCost', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=8, blank=True, null=True)  # Field name made lowercase.
    salescategory = models.CharField(db_column='SalesCategory', max_length=8, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4095, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    productclassid = models.CharField(db_column='ProductClassID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    productclassdescription = models.CharField(db_column='ProductClassDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expectedreceiptdate = models.DateTimeField(db_column='ExpectedReceiptDate', blank=True, null=True)  # Field name made lowercase.
    reorderincludeinpo = models.BooleanField(db_column='ReorderIncludeInPO')  # Field name made lowercase.
    reorderguidvendor = models.CharField(db_column='ReorderGUIDVendor', max_length=36, blank=True, null=True)  # Field name made lowercase.
    reorderunit = models.CharField(db_column='ReorderUnit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    reordercost = models.DecimalField(db_column='ReorderCost', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    reorderqty = models.DecimalField(db_column='ReorderQty', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    reordervendorproductid = models.CharField(db_column='ReorderVendorProductID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buildqty = models.DecimalField(db_column='BuildQty', max_digits=19, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    buildchecked = models.BooleanField(db_column='BuildChecked')  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productwarehousesummary'

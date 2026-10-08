from django.db import models


class Tbwhlocation(models.Model):
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", primary_key=True, max_length=36
    )  # Field name made lowercase.
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36
    )  # Field name made lowercase.
    description = models.CharField(
        db_column="Description",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    sequence = models.IntegerField(
        db_column="Sequence", blank=True, null=True
    )  # Field name made lowercase.
    group = models.CharField(
        db_column="Group",
        max_length=15,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    zone = models.CharField(
        db_column="Zone",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    active = models.BooleanField(db_column="Active")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tbwhlocation"
        unique_together = (("guidwarehouse", "description"),)


class Tbproductwarehouse(models.Model):
    guidproductwarehouse = models.CharField(
        db_column="GUIDProductWarehouse", primary_key=True, max_length=36
    )  # Field name made lowercase.
    guidproduct = models.CharField(
        db_column="GUIDProduct", max_length=36
    )  # Field name made lowercase.
    guidwarehouse = models.CharField(
        db_column="GUIDWarehouse", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    qtyreserved = models.DecimalField(
        db_column="QtyReserved", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    location = models.CharField(
        db_column="Location",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lastcost = models.DecimalField(
        db_column="LastCost", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    stdcost = models.DecimalField(
        db_column="StdCost", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    unitcost = models.DecimalField(
        db_column="UnitCost", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    value = models.DecimalField(
        db_column="Value", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    reorderpoint = models.DecimalField(
        db_column="ReorderPoint", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    stockinglevel = models.DecimalField(
        db_column="StockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    qtytoreorder = models.DecimalField(
        db_column="QtyToReorder", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    lastcountdate = models.DateTimeField(
        db_column="LastCountDate", blank=True, null=True
    )  # Field name made lowercase.
    note = models.TextField(
        db_column="Note",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    primarylocationstockinglevel = models.DecimalField(
        db_column="PrimaryLocationStockingLevel",
        max_digits=19,
        decimal_places=7,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    guidwhlocation = models.CharField(
        db_column="GUIDWHLocation", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    reorderincludeinpo = models.BooleanField(
        db_column="ReorderIncludeInPO"
    )  # Field name made lowercase.
    reorderguidvendor = models.CharField(
        db_column="ReorderGUIDVendor", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    reorderunit = models.CharField(
        db_column="ReorderUnit",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    reorderqty = models.DecimalField(
        db_column="ReorderQty", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    reordercost = models.DecimalField(
        db_column="ReorderCost", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    reordervendorproductid = models.CharField(
        db_column="ReorderVendorProductID",
        max_length=25,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    buildqty = models.DecimalField(
        db_column="BuildQty", max_digits=19, decimal_places=7, blank=True, null=True
    )  # Field name made lowercase.
    buildchecked = models.BooleanField(
        db_column="BuildChecked"
    )  # Field name made lowercase.
    deleted = models.BooleanField(db_column="Deleted")  # Field name made lowercase.
    reorder = models.BooleanField(db_column="Reorder")  # Field name made lowercase.
    build = models.BooleanField(db_column="Build")  # Field name made lowercase.
    reorderguidtaxcode = models.CharField(
        db_column="ReorderGUIDTaxCode", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tbproductwarehouse"
        unique_together = (("guidproduct", "guidwarehouse"),)

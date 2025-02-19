from product.models import *


class Volusionproducts(models.Model):
    """productcode = models.CharField(
        db_column="ProductCode",
        primary_key=True,
        max_length=150,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )"""

    product = models.OneToOneField(
        Tbproduct,
        on_delete=models.PROTECT,
        db_column="ProductCode",
        to_field="productid",
        primary_key=True,
        related_name="webproduct",
    )
    productname = models.CharField(
        db_column="ProductName",
        max_length=350,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    productdescription = models.TextField(
        db_column="ProductDescription",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    extinfo = models.TextField(
        db_column="ExtInfo",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    techspecs = models.TextField(
        db_column="TechSpecs",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    productprice = models.DecimalField(
        db_column="ProductPrice", max_digits=19, decimal_places=4, blank=True, null=True
    )
    lastmodby = models.CharField(
        db_column="LastModBy",
        max_length=10,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    lastmodified = models.DateTimeField(db_column="LastModified", blank=True, null=True)

    last_sync = models.DateTimeField(db_column="LastSync", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "volusionproducts"


class VolusionDescriptions(models.Model):
    productcode = models.CharField(
        primary_key=True, max_length=50, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    productdescription = models.TextField(
        db_collation="SQL_Latin1_General_CP1_CI_AS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "volusion_descriptions"


class TmpHpsPrices(models.Model):
    sku = models.CharField(
        db_column="SKU",
        primary_key=True,
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )  # Field name made lowercase.
    line = models.IntegerField(
        db_column="Line", blank=True, null=True
    )  # Field name made lowercase.
    product_type = models.TextField(
        db_column="Product_Type",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    status = models.CharField(
        db_column="Status",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    upc = models.BigIntegerField(
        db_column="UPC", blank=True, null=True
    )  # Field name made lowercase.
    msrp = models.DecimalField(
        db_column="MSRP", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    map = models.DecimalField(
        db_column="MAP", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    height = models.FloatField(
        db_column="HEIGHT", blank=True, null=True
    )  # Field name made lowercase.
    width = models.FloatField(
        db_column="WIDTH", blank=True, null=True
    )  # Field name made lowercase.
    length = models.FloatField(
        db_column="LENGTH", blank=True, null=True
    )  # Field name made lowercase.
    weight = models.FloatField(
        db_column="WEIGHT", blank=True, null=True
    )  # Field name made lowercase.
    changes = models.TextField(
        db_column="Changes",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    last_updated = models.DateField(
        db_column="Last_Updated", blank=True, null=True
    )  # Field name made lowercase.
    california_restricted = models.CharField(
        db_column="California_Restricted",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    street_legal_in_all_us_states = models.CharField(
        db_column="Street_Legal_In_All_US_States",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tmp_hps_prices"

from portal.models import *


class Volusionproducts(models.Model):
    productcode = models.CharField(
        db_column="ProductCode",
        primary_key=True,
        max_length=150,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
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

    class Meta:
        managed = False
        db_table = "volusionproducts"

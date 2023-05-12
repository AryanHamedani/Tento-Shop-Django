import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        _("Name"),
        max_length=50,
        blank=False,
        null=False,
    )
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        unique_together = (
            "name",
            "parent",
        )

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    rgb_hex = models.CharField(_("RGB hex"), max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SizeType(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SizeValue(models.Model):
    type = models.ForeignKey(SizeType, verbose_name=_("Type"), on_delete=models.PROTECT)
    value = models.CharField(_("Value"), max_length=50)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return f"{str(self.type)} : {self.value}"


class Material(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="brand_logos/")

    def __str__(self):
        return self.name


class Product(SoftDeletableModel, TimeStampedModel):
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
        related_name="products",
    )
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)
    image = models.ImageField(_("Image"), upload_to="products/thumbnail/%Y/%m/%d")
    description = models.TextField(_("Description"))
    material = models.ManyToManyField(
        Material, verbose_name=_("Material"), related_name="products"
    )
    available = models.BooleanField(_("Available"), default=True)
    brand = models.ForeignKey(
        Brand,
        verbose_name=_("Brand"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    # price = models.DecimalField(
    #     _("Price"), max_digits=10, decimal_places=0, null=False, blank=False
    # )
    # quantity = models.PositiveSmallIntegerField(_("Quantity in stock"))

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    # def is_in_stock(self):
    #     for variety in self.product_varieties.all():
    #         if variety.quantity > 0:
    #             return True
    #     return False

    # def available_colors(self):
    #     return [
    #         {"color": variety.color.name, "rgb_hex": variety.color.rgb_hex}
    #         for variety in self.product_varieties.filter(quantity__gt=0)
    #     ]

    # def total_stock_quantity(self):
    #     return sum([variety.quantity for variety in self.product_varieties.all()])

    def get_absolute_url(self):
        return f"product/{self.slug}/"

    def get_image_url(self):
        return "http://127.0.0.1:8000" + self.image.url

    # @property
    # def price(self):
    #     return self.product_varieties.order_by("price").first().price


class ProductVariety(SoftDeletableModel, TimeStampedModel):
    price = models.DecimalField(
        _("Price"), max_digits=10, decimal_places=0, null=False, blank=False
    )
    sku = models.UUIDField(
        _("SKU"),
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        auto_created=True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.PROTECT,
        related_name="product_varieties",
    )
    color = models.ForeignKey(
        Color,
        verbose_name=_("Color"),
        on_delete=models.PROTECT,
        related_name="product_varieties",
    )
    size = models.ForeignKey(
        SizeValue,
        verbose_name=("Size"),
        on_delete=models.PROTECT,
        related_name="product_varieties",
    )
    quantity = models.PositiveSmallIntegerField(_("Quantity in stock"))

    class Meta:
        ordering = ["-product"]
        verbose_name_plural = "Product Varieties"


# class ProductImageGallery(TimeStampedModel):
#     product = models.ForeignKey(
#         Product,
#         verbose_name=_("Product"),
#         on_delete=models.CASCADE,
#         related_name="images",
#     )
#     image = models.ImageField(
#         _("Image"), upload_to="products/product_image_gallery/%Y/%m/%d"
#     )

#     class Meta:
#         ordering = ["-product"]
#         verbose_name_plural = "Product Images Gallery"

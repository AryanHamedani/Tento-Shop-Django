from django.db import models  # noqa F401
from django.urls import reverse  # noqa F401
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel

from .managers import SubCategoriesManager


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=200, blank=False, null=False)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_category",
    )
    slug = models.SlugField(
        _("Slug"), unique=True, blank=False, null=False, max_length=200
    )
    objects = models.Manager()
    sub_categories = SubCategoriesManager()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Material(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class Product(SoftDeletableModel, TimeStampedModel):

    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"))
    image = models.ImageField(_("Image"), upload_to="products/%Y/%m/%d")
    description = models.TextField(_("Description"))
    material = models.ManyToManyField(
        Material, verbose_name=_("Material"), related_name="products"
    )
    available = models.BooleanField(_("Available"), default=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


class ProductVariety(SoftDeletableModel, TimeStampedModel):
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        "Color", verbose_name=_("Color"), on_delete=models.CASCADE
    )
    size = models.ForeignKey("Size", verbose_name=("Size"), on_delete=models.CASCADE)
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
    )
    quantity = models.PositiveSmallIntegerField(_("Quantity in stock"))


class Color(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    rgb_hex = models.CharField(_("RGB hex"), max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SizeType(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SizeValue(models.Model):
    type = models.ForeignKey(SizeType, verbose_name=_("Type"), on_delete=models.CASCADE)
    value = models.CharField(_("Value"), max_length=50)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return self.type


class ProductImageGallery:
    product_variety = models.ForeignKey(
        ProductVariety, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    image = models.ImageField(_("Image"), upload_to="product_image_gallery/")
    priority = models.PositiveSmallIntegerField(_("Priority"))

    class Meta:
        ordering = ["-priority"]

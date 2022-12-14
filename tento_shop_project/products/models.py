from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=50, blank=False, null=False)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    slug = models.SlugField(_("Category Slug"), unique=True, blank=False, null=False)


class Brand(models.Model):
    name = models.CharField(_("Brand Name"), max_length=50)
    logo = models.ImageField(_("Brand Logo"), upload_to="brand_logos")
    slug = models.SlugField(_("Brand Slug"))


class Product(SoftDeletableModel, TimeStampedModel):
    STATUS = Choices(
        (0, "AVAILABLE", _("Product is available to buy")),
        (1, "HIDDEN", _("Product is hidden")),
    )
    category = models.ForeignKey(
        Category, verbose_name=_("Product Category"), on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, verbose_name=_("Product Brand"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Product Name"), max_length=50)
    description = models.TextField(_("Product Description"))
    thumbnail = models.ImageField(
        _("Product Thumbnail"), upload_to="Product_Thumbnails"
    )
    slug = models.SlugField(_("Product slug"), unique=True)
    status = StatusField(verbose_name=_("Product Status"))
    status_changed = MonitorField(
        verbose_name=_("Product Status Change Date"), monitor="status"
    )


class Variation(models.Model):
    name = models.CharField(_("Variation name"), max_length=50, blank=False, null=False)


class VariationOption(models.Model):
    variation = models.ForeignKey(
        Variation,
        verbose_name=_("Variation of Option"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    value = models.CharField(_("Option Value"), max_length=50, blank=False, null=False)


class ProductItem(models.Model):
    product = models.ForeignKey(
        Product, verbose_name=_("Product of Item"), on_delete=models.CASCADE
    )
    options = models.ManyToManyField(VariationOption, verbose_name=_("Item Options"))
    price = models.DecimalField(
        _("Item Price"),
        max_digits=10,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )
    quantity = models.PositiveSmallIntegerField(
        _("Item quantity in stock"), blank=False, null=False, default=0
    )
    is_available = models.BooleanField(
        _("Is Item Available"), blank=False, null=False, default=True
    )


class ProductGallery(models.Model):
    image = models.ImageField(
        _("Product image"), upload_to="Product_Gallery", blank=False, null=False
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

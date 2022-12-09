from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=50)
    parent = models.ForeignKey(
        "products.Category",
        verbose_name=_("Parent Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class Brand(models.Model):
    name = models.CharField(_("Brand Name"), max_length=50)
    logo = models.ImageField(
        _("Brand Logo"), upload_to="brand_logos", height_field=500, width_field=500
    )


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_("Product Category"), on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, verbose_name=_("Product Brand"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Product Name"), max_length=50)
    description = models.TextField(_("Product Description"))
    slug = models.SlugField(_("Product slug"))
    # image field


class Variation(models.Model):
    name = models.CharField(_("Variation name"), max_length=50)
    # category = models.ForeignKey(Category, verbose_name=_("Variation Category"), on_delete=models.CASCADE)


class VariationOption(models.Model):
    variation = models.ForeignKey(
        Variation, verbose_name=_("Variation of Option"), on_delete=models.CASCADE
    )
    value = models.CharField(_("Option Value"), max_length=50)


class ProductItem(models.Model):
    product = models.ForeignKey(
        Product, verbose_name=_("Product of Item"), on_delete=models.CASCADE
    )
    options = models.ManyToManyField(VariationOption, verbose_name=_("Item Options"))
    price = models.DecimalField(_("Item Price"), max_digits=10, decimal_places=0)
    quantity = models.PositiveSmallIntegerField(_("Item quantity in the inventory"))
    is_available = models.BooleanField(_("Is Item Available"))

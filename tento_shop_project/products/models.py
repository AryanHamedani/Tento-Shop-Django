from django.db import models  # noqa F401
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.fields import MonitorField
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50, blank=False, null=False)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    slug = models.SlugField(_("Category Slug"), unique=True, blank=False, null=False)

    def get_absolute_url(self):
        """Get url for categories detail view.

        Returns:
            str: URL for category detail.

        """
        return reverse("products:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="brand_logos")

    def __str__(self):
        return self.name


class Product(SoftDeletableModel, TimeStampedModel):
    STATUS = Choices(
        (0, "AVAILABLE", _("Product is available to buy")),
        (1, "HIDDEN", _("Product is hidden")),
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Product Description"))
    thumbnail = models.ImageField(
        _("Product Thumbnail"), upload_to="Product_Thumbnails"
    )
    slug = models.SlugField(_("Slug"), unique=True)
    status = models.IntegerField(
        _("Product Status"),
        choices=STATUS,
        blank=False,
        null=False,
        default=STATUS.AVAILABLE,
    )
    status_changed = MonitorField(
        verbose_name=_("Last Status Change"), monitor="status"
    )

    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def get_absolute_url(self):
        """Get url for product's detail view.

        Returns:
            str: URL for product detail.

        """
        return reverse("products:detail", kwargs={"slug": self.slug})


class Color(models.Model):
    name = models.CharField(_("Color name"), max_length=50, blank=False, null=False)
    rgb_hex = models.CharField(_("RGB Hex of color"), max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    value = models.CharField(_("Size Value"), max_length=50, blank=False, null=False)

    def __str__(self):
        return self.value


class ProductConfig(models.Model):
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    color = models.ForeignKey(Color, verbose_name=_("Color"), on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name=_("Size"), on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        _("Item quantity in stock"), blank=False, null=False, default=0
    )


class ProductGallery(models.Model):
    image = models.ImageField(
        _("Image"), upload_to="Product_Gallery", blank=False, null=False
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(_("Name"), max_length=200, blank=False, null=False)
    parent = TreeForeignKey(
        "self",
        verbose_name=_("Parent"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    slug = models.SlugField(
        _("Slug"), unique=True, blank=False, null=False, max_length=200
    )

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:  # noqa E722
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append("/".join(ancestors[: i + 1]))
        return slugs

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


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


class Material(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="brand_logos/")
    slug = models.SlugField(_("Slug"))


class Product(SoftDeletableModel, TimeStampedModel):
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"))
    image = models.ImageField(_("Image"), upload_to="products/thumbnail/%Y/%m/%d")
    description = models.TextField(_("Description"))
    material = models.ManyToManyField(
        Material, verbose_name=_("Material"), related_name="products"
    )
    available = models.BooleanField(_("Available"), default=True)
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"), on_delete=models.CASCADE)

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
    size = models.ForeignKey(SizeValue, verbose_name=("Size"), on_delete=models.CASCADE)
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
    )
    quantity = models.PositiveSmallIntegerField(_("Quantity in stock"))


class ProductImageGallery(TimeStampedModel):
    product_variety = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    image = models.ImageField(
        _("Image"), upload_to="products/product_image_gallery/%Y/%m/%d"
    )
    priority = models.PositiveSmallIntegerField(_("Priority"))

    class Meta:
        ordering = ["-priority"]

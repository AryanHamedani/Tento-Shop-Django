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
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
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

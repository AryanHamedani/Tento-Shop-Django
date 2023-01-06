from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel


class MainCategory(models.Model):
    name = models.CharField(
        _("Name"), max_length=50, blank=False, null=False, unique=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"

    def __str__(self):
        return self.name

    def product_count(self):
        return sum([child.products.count() for child in self.children.all()])

    def sub_category_count(self):
        return self.children.count()


class SubCategory(models.Model):
    name = models.CharField(_("Name"), max_length=50, blank=False, null=False)
    parent = models.ForeignKey(
        MainCategory,
        verbose_name=_("Parent"),
        related_name="children",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        _("Slug"), unique=True, blank=False, null=False, max_length=200
    )

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

    def get_products_url(self):
        return "{base}?category={slug}".format(
            base=reverse("shop:product_list"), slug=self.slug
        )

    def product_count(self):
        return self.products.count()


class Color(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    rgb_hex = models.CharField(_("RGB hex"), max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def product_variety_count(self):
        return self.product_varieties.count()


class SizeType(models.Model):
    category = models.ForeignKey(
        SubCategory, verbose_name=_("Category"), on_delete=models.CASCADE
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
        return str(self.type) + self.value

    def product_variety_count(self):
        return self.product_varieties.count()


class Material(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name

    def product_count(self):
        return self.products.count()


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="brand_logos/")
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name

    def product_count(self):
        return self.products.count()


class Product(SoftDeletableModel, TimeStampedModel):
    category = models.ForeignKey(
        SubCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"))
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
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def is_in_stock(self):
        for variety in self.product_varieties.all():
            if variety.quantity > 0:
                return True
        return False

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    def available_colors(self):
        return [variety.color.name for variety in self.product_varieties.all()]

    def available_sizes(self):
        return [variety.size.value for variety in self.product_varieties.all()]

    def total_stock_quantity(self):
        return sum([variety.quantity for variety in self.product_varieties.all()])


class ProductVariety(SoftDeletableModel, TimeStampedModel):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="product_varieties",
    )
    color = models.ForeignKey(
        Color,
        verbose_name=_("Color"),
        on_delete=models.CASCADE,
        related_name="product_varieties",
    )
    size = models.ForeignKey(
        SizeValue,
        verbose_name=("Size"),
        on_delete=models.CASCADE,
        related_name="product_varieties",
    )
    quantity = models.PositiveSmallIntegerField(_("Quantity in stock"))

    @property
    def price(self):
        return self.product.price

    class Meta:
        ordering = ["-product"]
        verbose_name_plural = "Product Varieties"


class ProductImageGallery(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(
        _("Image"), upload_to="products/product_image_gallery/%Y/%m/%d"
    )
    priority = models.PositiveSmallIntegerField(_("Priority"))

    class Meta:
        ordering = ["-priority"]
        verbose_name_plural = "Product Images Gallery"

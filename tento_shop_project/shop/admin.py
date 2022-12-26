from django.contrib import admin  # noqa F401

from . import models  # noqa F401


@admin.register(models.MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    model = models.MainCategory
    list_display = ["name", "product_count", "sub_category_count"]
    search_fields = ["name"]


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    model = models.SubCategory
    list_display = ["name", "slug", "parent", "product_count"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["parent"]
    search_fields = ["name"]


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    model = models.Material
    list_display = ["name", "product_count"]
    search_fields = ["name"]


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    model = models.Brand
    list_display = ["name", "slug", "product_count"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(models.SizeType)
class SizeTypeAdmin(admin.ModelAdmin):
    model = models.SizeType
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(models.SizeValue)
class SizeValueAdmin(admin.ModelAdmin):
    model = models.SizeValue
    list_display = ["value", "type", "product_variety_count"]
    list_filter = ["type"]
    search_fields = ["value"]


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    model = models.Color
    list_display = ["name", "product_variety_count"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "available",
        "created",
        "modified",
        "price",
        "available_colors",
        "available_sizes",
        "total_stock_quantity",
    ]
    list_filter = [
        "available",
        "created",
        "modified",
        "price",
    ]
    list_editable = ["available"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.ProductVariety)
class ProductVarietyAdmin(admin.ModelAdmin):
    model = models.ProductVariety
    list_display = ["product", "size", "color", "quantity"]
    list_filter = ["product", "size", "color", "quantity"]
    search_fields = ["product"]


@admin.register(models.ProductImageGallery)
class ProductImageGalleryAdmin(admin.ModelAdmin):
    model = models.ProductImageGallery

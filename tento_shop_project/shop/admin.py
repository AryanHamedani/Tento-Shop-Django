from django.contrib import admin  # noqa F401

from .models import Category, Product  # noqa F401

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug"]
#     prepopulated_fields = {"slug": ("name",)}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug", "price", "available", "created", "modified"]
#     list_filter = ["available", "created", "modified"]
#     list_editable = ["price", "available"]
#     prepopulated_fields = {"slug": ("name",)}

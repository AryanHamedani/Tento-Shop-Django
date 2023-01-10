from django.contrib import admin  # noqa F401

from tento_shop_project.products import models

# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Product)
# admin.site.register(models.ProductVariety)
# admin.site.register(models.ProductImageGallery)
admin.site.register(models.Material)
admin.site.register(models.Color)
admin.site.register(models.SizeType)
admin.site.register(models.SizeValue)

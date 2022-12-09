from django.contrib import admin  # noqa F401

from tento_shop_project.products.models import (
    Brand,
    Category,
    Product,
    ProductItem,
    Variation,
    VariationOption,
)

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(Variation)
admin.site.register(VariationOption)

from django.contrib import admin  # noqa F401

from tento_shop_project.promotions.models import DiscountCode, Promotion

# Register your models here.
admin.site.register(Promotion)
admin.site.register(DiscountCode)

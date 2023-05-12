from django.contrib import admin  # noqa F401

from tento_shop_project.orders.models import Order, OrderItem

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)

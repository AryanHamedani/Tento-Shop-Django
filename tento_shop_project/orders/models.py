from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _

from tento_shop_project.products.models import ProductItem
from tento_shop_project.users.models import User


# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(
        User, verbose_name=_("Order Owner"), on_delete=models.CASCADE
    )
    description = models.TextField(_("Order Description"))
    order_date = models.DateTimeField(_("Order Date"), auto_now_add=True)
    total_price = models.DecimalField(_("Total Price"), max_digits=10, decimal_places=0)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE)
    item = models.ForeignKey(
        ProductItem, verbose_name=_("Product Item"), on_delete=models.CASCADE
    )
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(
        _("Ordered Quantity"), blank=False, null=False
    )

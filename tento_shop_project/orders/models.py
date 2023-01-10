from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField
from model_utils.models import SoftDeletableModel, TimeStampedModel

from tento_shop_project.products.models import Product
from tento_shop_project.users.models import User


# Create your models here.
class Order(TimeStampedModel, SoftDeletableModel):
    STATUS = Choices(
        ("PENDING", _("Pending for payment")),
        ("SUBMITTED", _("Order paid and submitted")),
        ("SUCCESS", _("Customer received order successfully")),
    )
    owner = models.ForeignKey(
        User,
        verbose_name=_("Order Owner"),
        on_delete=models.CASCADE,
        related_name="orders",
    )
    status = StatusField(verbose_name=_("Order Status"))
    status_changed = MonitorField(
        verbose_name=_("Order status change date"), monitor="status"
    )
    description = models.TextField(_("Order Description"), blank=True)
    total_price = models.DecimalField(
        _("Total Price"),
        max_digits=10,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )
    final_price = models.DecimalField(
        _("Final Price"),
        max_digits=10,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )

    def save(self, *args, **kwargs):
        if self.status == "SUBMITTED":
            for item in self.items.all():
                item.item.quantity -= item.quantity
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, verbose_name=_("Order"), on_delete=models.CASCADE, related_name="items"
    )
    item = models.ForeignKey(
        Product,
        verbose_name=_("Product Item"),
        on_delete=models.CASCADE,
        related_name="orders",
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        _("Ordered Quantity"), blank=False, null=False
    )

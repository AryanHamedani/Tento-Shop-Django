from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeFramedModel

from tento_shop_project.products.models import Product
from tento_shop_project.users.models import User


class Promotion(TimeFramedModel):
    item = models.ManyToManyField(Product, verbose_name=_("Product"))
    name = models.CharField(_("Name"), max_length=50, blank=True)
    rate = models.PositiveSmallIntegerField(
        _("Discount Percentage"), blank=False, null=False
    )
    max_amount = models.PositiveIntegerField(
        _("Discount Max Amount"), blank=False, null=False
    )
    description = models.TextField(_("Description"), blank=True)


class DiscountCode(models.Model):
    code = models.UUIDField(_("Code"), blank=False, null=False)
    rate = models.PositiveSmallIntegerField(_("Percentage"), blank=False, null=False)
    max_amount = models.PositiveIntegerField(_("Max Amount"), blank=False, null=False)
    available_to = models.ManyToManyField(
        User,
        verbose_name=_("Useable by"),
    )

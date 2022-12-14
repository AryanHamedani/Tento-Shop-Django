from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeFramedModel

from tento_shop_project.products.models import ProductItem
from tento_shop_project.users.models import User


class Promotion(TimeFramedModel):
    item = models.ManyToManyField(ProductItem, verbose_name=_("Item To Promote"))
    name = models.CharField(_("Promotion Name"), max_length=50, blank=True)
    rate = models.PositiveSmallIntegerField(
        _("Discount Percentage"), blank=False, null=False
    )
    max_amount = models.PositiveIntegerField(
        _("Discount Max Amount"), blank=False, null=False
    )
    description = models.TextField(_("Promotion Description"), blank=True)


class DiscountCode(models.Model):
    code = models.UUIDField(_("Discount Code"), blank=False, null=False)
    rate = models.PositiveSmallIntegerField(
        _("Discount Percentage"), blank=False, null=False
    )
    max_amount = models.PositiveIntegerField(
        _("Discount Max Amount"), blank=False, null=False
    )
    available_to = models.ManyToManyField(
        User,
        verbose_name=_("Useable by"),
    )

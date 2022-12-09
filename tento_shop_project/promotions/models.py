from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _

from tento_shop_project.products.models import ProductItem
from tento_shop_project.users.models import User


# Create your models here.
class Promotion(models.Model):
    item = models.ManyToManyField(ProductItem, verbose_name=_("Item To Promote"))
    name = models.CharField(_("Promotion Name"), max_length=50, blank=True)
    rate = models.PositiveSmallIntegerField(_("Discount Percentage"))
    max_amount = models.PositiveIntegerField(_("Discount Max Amount"))
    description = models.TextField(_("Promotion Description"), blank=True)
    start_date = models.DateTimeField(
        _("Promotion Start Date and Time"), auto_now=False, auto_now_add=False
    )
    end_date = models.DateTimeField(
        _("Promotion End Date and Time"), auto_now=False, auto_now_add=False
    )


class DiscountCode(models.Model):
    code = models.UUIDField(_("Discount Code"))
    rate = models.PositiveSmallIntegerField(_("Discount Percentage"))
    max_amount = models.PositiveIntegerField(_("Discount Max Amount"))
    available_to = models.ManyToManyField(User, verbose_name=_("Useable by"))

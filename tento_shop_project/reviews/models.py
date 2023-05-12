from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from tento_shop_project.products.models import Product
from tento_shop_project.users.models import User


class Review(TimeStampedModel):
    owner = models.ForeignKey(
        User,
        verbose_name=_("Reviewer"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    rate = models.PositiveSmallIntegerField(_("Rate (from 5)"), blank=False, null=False)
    title = models.CharField(_("Review Title"), max_length=100, blank=False, null=False)
    context = models.TextField(_("Review Context"), blank=False, null=False)

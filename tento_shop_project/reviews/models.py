from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _

from tento_shop_project.products.models import ProductItem
from tento_shop_project.users.models import User

# Create your models here.


class Review(models.Model):
    owner = models.ForeignKey(
        User, verbose_name=_("Reviewer"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        ProductItem, verbose_name=_("Reviewed Product"), on_delete=models.CASCADE
    )
    rate = models.PositiveSmallIntegerField(_("Rate (from 10)"))
    title = models.CharField(_("Review Title"), max_length=100)
    context = models.TextField(_("Review Context"))

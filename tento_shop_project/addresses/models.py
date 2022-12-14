from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import AddressModel

from tento_shop_project.users.models import User


class Province(models.Model):
    name = models.CharField(
        _("Province name"), max_length=50, blank=False, null=False, unique=True
    )

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    province = models.ForeignKey(
        Province, verbose_name=_("Province name"), on_delete=models.CASCADE
    )
    name = models.CharField(
        _("City name"), max_length=50, blank=False, null=False, unique=True
    )

    def __str__(self) -> str:
        return self.name


class Address(AddressModel):
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.CASCADE)
    title = models.CharField(_("Address Title"), max_length=50, blank=True, null=True)
    owner = models.ForeignKey(
        User, verbose_name=_("Address owner"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        if self.title:
            return self.title
        return self.postal_code

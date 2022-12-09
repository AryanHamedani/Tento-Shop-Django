from django.contrib.gis.db import models as gis_models
from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _

from tento_shop_project.users.models import User


# Create your models here.
class Province(models.Model):
    name = models.CharField(
        _("Province name"), max_length=50, blank=False, null=False, unique=True
    )


class City(models.Model):
    province = models.ForeignKey(
        Province, verbose_name=_("Province name"), on_delete=models.CASCADE
    )
    name = models.CharField(
        _("City name"), max_length=50, blank=False, null=False, unique=True
    )


class Address(models.Model):
    title = models.CharField(_("Address Title"), max_length=50, blank=True, null=True)
    street = models.TextField(_("Street Address"), blank=False, null=False)
    number = models.PositiveSmallIntegerField(_("Building Number"))
    unit = models.PositiveSmallIntegerField(_("Unit Number"))
    postal_code = models.CharField(
        _("Postal Code"), max_length=10, blank=False, null=False
    )
    location = gis_models.PointField(_("Address Location"))
    owner = models.ForeignKey(
        User, verbose_name=_("Address owner"), on_delete=models.CASCADE
    )

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressModel(models.Model):
    street = models.TextField(_("Street Address"))
    number = models.PositiveSmallIntegerField(_("Building Number"))
    unit = models.PositiveSmallIntegerField(_("Unit Number"))
    postal_code = models.CharField(_("Postal Code"), max_length=10)
    location = gis_models.PointField(_("Address Location"))

    class Meta:
        abstract = True

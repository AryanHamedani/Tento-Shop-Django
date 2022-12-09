from django.contrib.gis.db import models as gis_models
from django.db import models  # noqa F401
from django.utils.translation import gettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

from tento_shop_project.core.managers import SoftDeletableManager


# Create your models here.
class AddressModel(models.Model):
    street = models.TextField(_("Street Address"))
    number = models.PositiveSmallIntegerField(_("Building Number"))
    unit = models.PositiveSmallIntegerField(_("Unit Number"))
    postal_code = models.CharField(_("Postal Code"), max_length=10)
    location = gis_models.PointField(_("Address Location"))

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    """
    An abstract base class model that provides ``start``
    and ``end`` fields to record a timeframe.

    """

    start = models.DateTimeField(_("start"), null=True, blank=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)

    class Meta:
        abstract = True


class SoftDeletableModel(models.Model):
    """
    An abstract base class model with a ``is_removed`` field that
    marks entries that are not going to be used anymore, but are
    kept in db for any reason.
    Default manager returns only not-removed entries.
    """

    is_removed = models.BooleanField(default=False)
    # is index true

    class Meta:
        abstract = True

    objects = SoftDeletableManager(_emit_deprecation_warnings=True)
    available_objects = SoftDeletableManager()
    all_objects = models.Manager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        Soft delete object (set its ``is_removed`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        if soft:
            self.is_removed = True
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)


class TimeStampedModel(models.Model):
    # be mixin
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """

    created = AutoCreatedField(_("created"))
    modified = AutoLastModifiedField(_("modified"))

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get("update_fields", None)
        if update_fields:
            kwargs["update_fields"] = set(update_fields).union({"modified"})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True

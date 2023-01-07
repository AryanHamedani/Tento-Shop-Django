from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneNumberField(
        region="IR",
        verbose_name=_("Phone Number"),
        unique=True,
        help_text=_("Required. Iranian Phone Number format."),
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        _str = f"{self.id} {self.phone_number}"
        return _str.strip()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_active:
            Profile.objects.create(owner=self)


class Profile(SoftDeletableModel, TimeStampedModel):
    class Gender(models.IntegerChoices):
        MALE = 0, _("Male")
        FEMALE = 1, _("Female")
        NONE = 2, _("None of binary")

    owner = models.OneToOneField(
        User,
        verbose_name=_("Profile Owner"),
        on_delete=models.CASCADE,
        related_name="profile",
    )
    first_name = models.CharField(_("First Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True)
    gender = models.IntegerField(
        _("Gender"), choices=Gender.choices, blank=True, null=True
    )
    national_code = models.CharField(
        _("National Code"), max_length=12, blank=True, null=True, unique=True
    )

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()


class Province(models.Model):
    name = models.CharField(
        _("Province name"), max_length=50, blank=False, null=False, unique=True
    )

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    province = models.ForeignKey(
        Province, verbose_name=_("Province name"), on_delete=models.PROTECT
    )
    name = models.CharField(
        _("City name"), max_length=50, blank=False, null=False, unique=True
    )

    def __str__(self) -> str:
        return self.name


class Address(TimeStampedModel):
    owner = models.ForeignKey(
        User, verbose_name=_("Owner"), on_delete=models.DO_NOTHING
    )
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)
    location = gis_models.PointField(_("Location"))
    street = models.TextField(_("Street"))
    number = models.PositiveSmallIntegerField(_("Building Number"))
    unit = models.PositiveSmallIntegerField(_("Unit Number"))
    postal_code = models.CharField(_("Postal Code"), max_length=10)

    def __str__(self) -> str:
        _str = f"{self.owner.phone_number} - {self.id} - {self.postal_code}"
        return _str

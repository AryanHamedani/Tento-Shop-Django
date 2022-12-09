from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Default custom user model for Tento Shop Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 0, _("Male")
        FEMALE = 1, _("Female")
        NONE = 2, _("None of binary")

    owner = models.OneToOneField(
        User, verbose_name=_("Profile Owner"), on_delete=models.CASCADE
    )
    first_name = models.CharField(_("First Name"), max_length=50, blank=False)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=False)
    gender = models.IntegerField(
        _("Gender"), choices=Gender.choices, blank=True, null=True
    )
    phone = PhoneNumberField(
        region="IR", blank=True, null=True, unique=True, verbose_name=_("Phone Number")
    )
    national_code = models.CharField(
        _("National Code"), max_length=12, blank=True, null=True, unique=True
    )

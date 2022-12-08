from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.addresses"
    verbose_name = _("Addresses")

    def ready(self):
        try:
            import tento_shop_project.addresses.signals  # noqa F401
        except ImportError:
            pass

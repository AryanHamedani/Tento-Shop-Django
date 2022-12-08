from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.address"
    verbose_name = _("Address")

    def ready(self):
        try:
            import tento_shop_project.address.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CartConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.cart"
    verbose_name = _("Cart")

    def ready(self):
        try:
            import tento_shop_project.cart.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PromotionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.promotions"
    verbose_name = _("Promotions")

    def ready(self):
        try:
            import tento_shop_project.promotions.signals  # noqa F401
        except ImportError:
            pass

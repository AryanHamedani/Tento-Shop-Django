from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PromotionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.promotion"
    verbose_name = _("Promotion")

    def ready(self):
        try:
            import tento_shop_project.promotion.signals  # noqa F401
        except ImportError:
            pass

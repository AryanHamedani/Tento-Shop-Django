from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.core"
    verbose_name = _("Core")

    def ready(self):
        try:
            import tento_shop_project.core.signals  # noqa F401
        except ImportError:
            pass

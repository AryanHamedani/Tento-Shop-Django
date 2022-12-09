from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReviewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tento_shop_project.reviews"
    verbose_name = _("Reviews")

    def ready(self):
        try:
            import tento_shop_project.reviews.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tento_shop_project.users"
    verbose_name = _("Users")

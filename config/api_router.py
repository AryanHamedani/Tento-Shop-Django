from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tento_shop_project.shop.api.views import ProductViewSet
from tento_shop_project.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("shop", ProductViewSet)


app_name = "api"
urlpatterns = router.urls

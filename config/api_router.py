from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tento_shop_project.orders.api.views import OrderViewSet
from tento_shop_project.shop.api.views import ProductViewSet
from tento_shop_project.users.api.views import (
    AddressViewSet,
    ProfileViewSet,
    UserViewSet,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("profiles", ProfileViewSet, basename="profiles")
router.register("addresses", AddressViewSet)

router.register("shop", ProductViewSet)
router.register("orders", OrderViewSet, basename="orders")


app_name = "api"
urlpatterns = router.urls

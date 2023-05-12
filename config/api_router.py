from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# from tento_shop_project.orders.api.views import OrderViewSet
from tento_shop_project.products.api.viewsets import (
    CategoryDetailView,
    ProductDetailViewSet,
    ProductListViewSet,
)
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

router.register("category", CategoryDetailView, basename="category")
router.register("products", ProductListViewSet, basename="products")
router.register("product", ProductDetailViewSet, basename="product")

# router.register("orders", OrderViewSet, basename="orders")


app_name = "api"
urlpatterns = router.urls

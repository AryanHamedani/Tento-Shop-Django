from django.urls import path

from .views import CartView

app_name = "cart"
urlpatterns = [
    path("", CartView.as_view(), name="get_cart"),
    path("<int:product_id>/", CartView.as_view(), name="add_to_cart"),
]

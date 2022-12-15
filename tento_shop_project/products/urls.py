from django.urls import path

from tento_shop_project.products.views import ProductDetailView

app_name = "products"

urlpatterns = [path("<slug:slug>", ProductDetailView.as_view(), name="detail")]

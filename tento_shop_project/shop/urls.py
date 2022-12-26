from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path(
        "products/",
        views.ProductListView.as_view(),
        name="product_list",
    ),
    path(
        "<int:id>/<slug:slug>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("categories/", views.CategoryListView.as_view(), name="category_list")
    # path("product/<str:sku>", views.ProductView.as_view(), name="productTemplate"),
]

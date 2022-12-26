from django.shortcuts import render  # noqa F401
from django.views import generic

from tento_shop_project.products.models import Product

# Create your views here.


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

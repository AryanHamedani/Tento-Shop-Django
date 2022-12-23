from django.shortcuts import render
from django.views import generic

from .models import MainCategory, Product


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 9
    template_name = "shop/product/list.html"
    context_object_name = "products"

    def get_queryset(self):
        query_set = super().get_queryset()
        if self.request.GET.get("category"):
            return query_set.filter(category__slug=self.request.GET.get("category"))
        return query_set


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = "product"
    template_name = "shop/product/detail.html"


class CategoryListView(generic.ListView):
    model = MainCategory
    template_name = "shop/category/list.html"
    context_object_name = "categories"


class LandingPageView(generic.View):
    def get(self, request):
        latest_products = Product.objects.filter(available=True).order_by("created")[:4]
        return render(request, "pages/home.html", {"latest_products": latest_products})

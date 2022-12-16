from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Category, Product


class ProductListView(generic.ListView):
    template_name = "shop/product/list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        self.category = None
        self.categories = Category.objects.all()
        self.products = Product.objects.filter(available=True)
        if self.kwargs["category_slug"]:
            self.category = get_object_or_404(
                Category, slug=self.kwargs["category_slug"]
            )
            self.products = self.products.filter(
                Q(category__in=self.category.sub_category.all())
                | Q(category=self.category)
            )
        return self.products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.categories
        context["category"] = self.category


class ProductDetailView(generic.DeleteView):
    model = Product
    template_name = "shop/product/detail.html"

    def get_queryset(self):
        self.product = get_object_or_404(
            Product, id=self.kwargs["id"], slug=self.kwargs["slug"], available=True
        )

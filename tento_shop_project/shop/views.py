from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Category, Product


class ProductListView(generic.View):
    def get(self, request, category_slug=None):
        self.category = None
        self.categories = Category.objects.all()
        self.products = Product.objects.filter(available=True)
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            self.products = self.products.filter(
                Q(category__in=self.category.sub_category.all())
                | Q(category=self.category)
            )
        return render(
            request,
            "shop/product/list.html",
            context={
                "category": self.category,
                "categories": self.categories,
                "products": self.products,
            },
        )


class ProductDetailView(generic.View):
    context_object_name = "product"
    template_name = "shop/product/detail.html"

    def get_queryset(self):

        return super().get_queryset()

    def get(self, request, id, slug):
        self.product = get_object_or_404(Product, id=id, slug=slug, available=True)
        return render(
            request, "shop/product/detail.html", context={"product": self.product}
        )

from django.shortcuts import get_object_or_404, redirect, render  # noqa F401
from django.views import generic

from tento_shop_project.shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(generic.View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product,
                quantity=cd["quantity"],
                override_quantity=cd["override"],
            )
        return redirect("cart:cart_detail")

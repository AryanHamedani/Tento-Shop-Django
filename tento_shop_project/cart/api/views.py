from rest_framework.response import Response
from rest_framework.views import APIView

from tento_shop_project.cart.cart import Cart
from tento_shop_project.shop.api.serializers import ProductVarietySerializer
from tento_shop_project.shop.models import ProductVariety


class CartView(APIView):
    def get(self, request):
        cart = Cart(request=request)
        return Response(
            {
                "total_quantity": len(cart),
                "total_price": cart.get_total_price(),
                "items": [
                    {
                        "total_price": item["total_price"],
                        "quantity": item["quantity"],
                        "product": ProductVarietySerializer(item["product"]).data,
                    }
                    for item in cart
                ],
            }
        )

    def post(self, request, product_id):
        cart = Cart(request=request)
        try:
            product_variety = ProductVariety.objects.get(id=product_id)
        except ProductVariety.DoesNotExist:
            return Response({"message": "Product Does Not Exist"}, 404)
        else:
            if product_variety.product.available and product_variety.quantity > 0:
                try:
                    cart.cart[str(product_id)]
                except KeyError:
                    cart.add(product_variety)
                else:
                    if (
                        cart.cart[str(product_id)]["quantity"] + 1
                        <= product_variety.quantity
                    ):
                        cart.add(product_variety)
                    else:
                        Response({"message": "Product Is Out of Stock"}, 403)

            else:
                Response({"message": "Product Is Not Available"}, 403)
            return Response({"message": "Success"})

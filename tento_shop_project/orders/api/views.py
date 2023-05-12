from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView  # Noqa 401
from rest_framework.viewsets import GenericViewSet

from tento_shop_project.cart.cart import Cart  # Noqa 401
from tento_shop_project.orders.models import Order, OrderItem  # Noqa 401
from tento_shop_project.products.models import Product  # Noqa 401

from .serializers import OrderSerializer

# class OrderViewSet(
#     CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
# ):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Order.objects.filter(owner=user)

#     def create(self, request, *args, **kwargs):
#         cart = Cart(request)
#         # product_ids = cart.keys()
#         # products = ProductVariety.objects.filter(id__in=product_ids)
#         for _id in cart:
#             if cart[_id]["product"].quantity >= cart[_id]["quantity"]:
#                 cart[_id]["product"].quantity -= cart[_id]["quantity"]
#                 cart[_id]["product"].save()
#                 item = OrderItem(order = self)


#         super().create(request, *args, **kwargs)


# class OrderView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):


#     def post(self, request):
#         pass


class OrderViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

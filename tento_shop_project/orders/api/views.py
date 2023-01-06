from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView  # Noqa 401
from rest_framework.viewsets import GenericViewSet

from tento_shop_project.orders.models import Order  # Noqa 401

from .serializers import OrderSerializer


class OrderViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    serializer_class = OrderSerializer

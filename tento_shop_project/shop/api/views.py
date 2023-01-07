from rest_framework import status  # Noqa 401
from rest_framework.decorators import action  # Noqa 401
from rest_framework.mixins import (  # Noqa 401
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response  # Noqa 401
from rest_framework.viewsets import GenericViewSet

from tento_shop_project.shop.models import Product

from .serializers import ProductSerializer


class ProductViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "slug"

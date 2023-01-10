from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from tento_shop_project.products import models

from . import serializers


class ProductListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Product.objects.filter(available=True)
    serializer_class = serializers.ProductListSerializer
    lookup_field = "slug"


class ProductDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    lookup_field = "slug"


class CategoryDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Category.objects.all()
    lookup_field = "id"
    serializer_class = serializers.CategorySerializer

from rest_framework import serializers

from tento_shop_project.shop import models


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    material = serializers.StringRelatedField(read_only=True, many=True)
    # total_quantity = serializers.

    class Meta:
        model = models.Product
        fields = [
            "category",
            "name",
            "slug",
            "image",
            "available",
            "brand",
            "price",
            "material",
            "description",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:product-detail", "lookup_field": "slug"}
        }

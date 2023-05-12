from rest_framework import serializers

from tento_shop_project.shop import models


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    material = serializers.StringRelatedField(read_only=True, many=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=0)
    category = serializers.StringRelatedField(read_only=True)
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


class ProductVarietySerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    color = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.ProductVariety
        fields = ["product", "color", "size"]

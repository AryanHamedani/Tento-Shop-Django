from rest_framework import serializers

from tento_shop_project.orders import models


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    items = serializers.SlugRelatedField(read_only=True, many=True, slug_field="price")
    # total_quantity = serializers.

    class Meta:
        model = models.Order
        fields = [
            "status",
            "status_changed",
            "description",
            "total_price",
            "final_price",
            "created",
            "modified",
            "items",
            "owner",
        ]

        # extra_kwargs = {
        #     "url": {"view_name": "api:order-detail", "lookup_field": "id"}
        # }

from rest_framework import serializers

from tento_shop_project.orders import models


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    items = serializers.StringRelatedField(read_only=True, many=True)
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
        ]

        # extra_kwargs = {
        #     "url": {"view_name": "api:order-detail", "lookup_field": "id"}
        # }

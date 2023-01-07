from rest_framework import serializers

from tento_shop_project.orders import models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    # items = serializers.SerializerMethodField(read_only=True, many=True)
    items = OrderItemSerializer(many=True)

    # total_quantity = serializers.

    def get_items(self, obj):
        items = obj.items.all()
        return OrderItemSerializer(items, many=True).data

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

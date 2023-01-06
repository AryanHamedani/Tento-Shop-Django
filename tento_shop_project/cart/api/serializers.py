from rest_framework import serializers

from tento_shop_project.shop.api.serializers import ProductVarietySerializer


class CartAddItemSerializer(serializers.Serializer):
    item = ProductVarietySerializer()
    quantity = serializers.IntegerField(max_value=item.quantity)
    override = serializers.BooleanField(
        required=False,
        initial=False,
    )

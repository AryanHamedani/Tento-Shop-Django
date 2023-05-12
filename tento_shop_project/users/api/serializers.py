from django.contrib.auth import get_user_model
from rest_framework import serializers

from tento_shop_project.users import models as user_models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ["username", "password"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = user_models.Profile
        fields = "__all__"

        extra_kwargs = {
            "url": {"view_name": "api:profile-detail", "lookup_field": "owner"}
        }


class CitySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = user_models.City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer

    class Meta:
        model = user_models.Address
        fields = "__all__"

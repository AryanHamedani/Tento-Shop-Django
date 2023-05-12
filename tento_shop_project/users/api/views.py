from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response  # Noqa 401
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from tento_shop_project.users.models import Address

from . import serializers as user_serializers

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = user_serializers.UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = user_serializers.ProfileSerializer
    lookup_field = "owner"


class AddressViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = user_serializers.AddressSerializer
    queryset = Address.objects.all()
    lookup_field = "owner"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(owner__id=self.request.user.id)


class SignUpView(APIView):
    def get(self, request):
        pass


class ForgetPasswordView(APIView):
    pass


# class


class ProfileView(ModelViewSet):
    pass

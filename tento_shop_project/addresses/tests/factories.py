from factory import Faker
from factory.django import DjangoModelFactory

from tento_shop_project.addresses.models import Province


class ProvinceFactory(DjangoModelFactory):

    name = Faker("administrative_unit", locale="fa-IR")

    class Meta:
        model = Province
        django_get_or_create = ["name"]

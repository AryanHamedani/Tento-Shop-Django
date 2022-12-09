import pytest  # noqa F401

from tento_shop_project.addresses.models import Province

# from tento_shop_project.addresses.tests.factories import ProvinceFactory


def test_province_creation(province: Province):
    assert Province.objects.get(name=province.name) == province


def test_province_name(province: Province):
    assert province.name


# @pytest.mark.django_db
# def test_province_name_is_unique():
#     assert ProvinceFactory.create_batch(2, name="Tehran")

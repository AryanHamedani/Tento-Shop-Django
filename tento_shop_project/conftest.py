import pytest

from tento_shop_project.addresses.models import Province
from tento_shop_project.addresses.tests.factories import ProvinceFactory
from tento_shop_project.users.models import User
from tento_shop_project.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def province(db) -> Province:
    return ProvinceFactory()

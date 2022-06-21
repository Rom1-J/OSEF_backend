import pytest

from osef.apps.transactions.tests.factories import (
    FileFactory,
    TransactionFactory,
)
from osef.apps.users.models import User
from osef.apps.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def user1() -> User:
    return UserFactory()


@pytest.fixture
def user2() -> User:
    return UserFactory()


@pytest.fixture
def transaction() -> User:
    return TransactionFactory()


@pytest.fixture
def file() -> User:
    return FileFactory()

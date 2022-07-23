import pytest
from rest_framework.test import APIRequestFactory

from osef.apps.notifications.models import Notification
from osef.apps.notifications.tests.factories import NotificationFactory
from osef.apps.transactions.models import File, Transaction
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
def arf() -> APIRequestFactory:
    return APIRequestFactory(enforce_csrf_checks=True)


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
def transaction() -> Transaction:
    return TransactionFactory()


@pytest.fixture
def file() -> File:
    return FileFactory()


@pytest.fixture
def notification() -> Notification:
    return NotificationFactory()

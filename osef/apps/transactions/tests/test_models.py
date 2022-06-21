import pytest

from osef.apps.transactions.models import Transaction
from osef.apps.transactions.tests.fixtures import (
    transaction_fixture,
    user_fixture,
)

pytestmark = pytest.mark.django_db


# noinspection PyShadowingNames
def test_transaction_get_file_count(transaction: Transaction):
    assert transaction.get_file_count() == transaction.files.count()


# =============================================================================

transaction = transaction_fixture
user1 = user_fixture
user2 = user_fixture

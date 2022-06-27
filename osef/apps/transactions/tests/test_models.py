import pytest

from osef.apps.transactions.models import Transaction

pytestmark = pytest.mark.django_db


# noinspection PyShadowingNames
def test_transaction_get_file_count(transaction: Transaction):
    assert transaction.get_file_count() == transaction.files.count()

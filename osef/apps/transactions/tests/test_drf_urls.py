import pytest
from django.urls import resolve, reverse

from osef.apps.transactions.models import Transaction

pytestmark = pytest.mark.django_db


class TestTransactionAPIUrls:
    def test_transaction_detail(self, transaction: Transaction):
        assert (
            reverse(
                "api:transaction-detail",
                kwargs={"token": transaction.token}
            ) == f"/api/transactions/{transaction.token}/"
        )
        assert resolve(
            f"/api/transactions/{transaction.token}/"
        ).view_name == "api:transaction-detail"

    def test_user_list(self):
        assert reverse("api:transaction-list") == "/api/transactions/"
        assert resolve("/api/transactions/").view_name == "api:transaction-list"

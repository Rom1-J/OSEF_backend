import pytest
from django.test import RequestFactory

from osef.apps.transactions.api.views import TransactionViewSet
from osef.apps.transactions.models import Transaction

pytestmark = pytest.mark.django_db


class TestTransactionsViewSet:
    def test_get_queryset(self, transaction: Transaction, rf: RequestFactory):
        view = TransactionViewSet()
        request = rf.get("/fake-url/")
        request.user = transaction.user2

        view.request = request

        assert transaction in view.get_queryset()

    def test_me(self, transaction: Transaction, rf: RequestFactory):
        view_detail = TransactionViewSet.as_view({"get": "retrieve"})
        request = rf.get("/fake-url/")
        request.user = transaction.user2

        response = view_detail(request, token=transaction.token)

        cleaned_data = response.data["data"]
        del cleaned_data["created_at"]  # fails when test for TZ
        del cleaned_data["updated_at"]  # fails when test for TZ

        assert cleaned_data == {
            "token": str(transaction.token),
            "user1": {
                "username": str(transaction.user1),
                "pub_key": str(transaction.user1.pub_key),
            },
            "user2": {
                "username": str(transaction.user2),
                "pub_key": str(transaction.user2.pub_key),
            },
            "accepted": True,
        }

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from osef.apps.transactions.models import File, Transaction
from osef.apps.users.models import User

pytestmark = pytest.mark.django_db


class TestTransactionAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:transactions_transaction_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:transactions_transaction_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    # noinspection PyShadowingNames
    def test_add(self, admin_client, user1: User, user2: User):
        url = reverse("admin:transactions_transaction_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "user1": user1.id,
                "user2": user2.id,
            },
        )
        assert response.status_code == 302
        assert Transaction.objects.filter(user1=user1).exists()

    # noinspection PyShadowingNames
    def test_view_transaction(self, admin_client, transaction: Transaction):
        url = reverse(
            "admin:transactions_transaction_change",
            kwargs={"object_id": transaction.pk},
        )
        response = admin_client.get(url)
        assert response.status_code == 200


class TestFileAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:transactions_file_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:transactions_file_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    # noinspection PyShadowingNames
    def test_add(self, admin_client, transaction: Transaction):
        url = reverse("admin:transactions_file_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "file": SimpleUploadedFile(
                    "file.txt", b"file content", content_type="text/plain"
                ),
                "nonce": "randomNonce",
                "transaction": transaction.token,
                "owner": transaction.user1.id,
                "receiver": transaction.user2.id,
            },
        )
        assert response.status_code == 302
        assert File.objects.filter(owner=transaction.user1).exists()

    # noinspection PyShadowingNames
    def test_view_transaction(self, admin_client, file: File):
        url = reverse(
            "admin:transactions_file_change",
            kwargs={"object_id": file.pk},
        )
        response = admin_client.get(url)
        assert response.status_code == 200

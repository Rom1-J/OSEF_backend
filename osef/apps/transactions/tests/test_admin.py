import pytest
from django.urls import reverse

from osef.apps.transactions.models import Transaction
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
        assert Transaction.objects.filter(user1__username="JohnDoe").exists()

    def test_view_transaction(self, admin_client, transaction: Transaction):
        url = reverse(
            "admin:transactions_transaction_change",
            kwargs={"object_id": transaction.pk},
        )
        response = admin_client.get(url)
        assert response.status_code == 200


# =============================================================================


@pytest.fixture
def user1():
    user = User.objects.create(
        username="JohnDoe",
        first_name="John",
        last_name="Doe",
        email="john@doe.fr",
    )

    user.set_unusable_password()
    user.save()

    return user


@pytest.fixture
def user2():
    user = User.objects.create(
        username="JaneDoe",
        first_name="Jane",
        last_name="Doe",
        email="jane@doe.fr",
    )

    user.set_unusable_password()
    user.save()

    return user


@pytest.fixture
def transaction(user1: User, user2: User):
    transaction = Transaction.objects.create(
        user1=user1,
        user2=user2,
    )
    transaction.save()

    return transaction

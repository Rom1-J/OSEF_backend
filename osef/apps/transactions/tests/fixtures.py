import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from factory import Faker

from osef.apps.transactions.models import File, Transaction
from osef.apps.users.models import User


@pytest.fixture
def user_fixture():
    user = User.objects.create(
        username=Faker("user_name"),
        first_name=Faker("first_name"),
        last_name=Faker("last_name"),
        email=Faker("email"),
    )

    user.set_unusable_password()
    user.save()

    return user


@pytest.fixture
def transaction_fixture(user1: User, user2: User):
    transaction = Transaction.objects.create(
        user1=user1,
        user2=user2,
    )
    transaction.save()

    return transaction


@pytest.fixture
def file_fixture(transaction: Transaction):
    file = File.objects.create(
        file=SimpleUploadedFile(
            "file.txt", b"file content", content_type="text/plain"
        ),
        transaction=transaction,
        owner=transaction.user1,
        receiver=transaction.user2,
    )
    file.save()

    return file

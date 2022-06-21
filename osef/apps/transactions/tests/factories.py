import uuid

from django.core.files.uploadedfile import SimpleUploadedFile
from factory.django import DjangoModelFactory

from osef.apps.users.tests.factories import UserFactory

from ..models import File, Transaction


class TransactionFactory(DjangoModelFactory):
    token = uuid.uuid4()
    user1 = UserFactory
    user2 = UserFactory

    class Meta:
        model = Transaction
        django_get_or_create = ["token"]


class FileFactory(DjangoModelFactory):
    id = uuid.uuid4()
    file = SimpleUploadedFile(
        "file.txt", b"file content", content_type="text/plain"
    )

    owner = UserFactory
    receiver = UserFactory

    transaction = TransactionFactory

    class Meta:
        model = File
        django_get_or_create = ["id"]

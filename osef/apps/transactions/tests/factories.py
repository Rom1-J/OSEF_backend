from factory.django import DjangoModelFactory

from ..models import Transaction


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = Transaction
        django_get_or_create = ["token"]

import uuid

from factory.django import DjangoModelFactory

from osef.apps.users.tests.factories import UserFactory

from ..models import Notification


class NotificationFactory(DjangoModelFactory):
    id = uuid.uuid4()
    emitter = UserFactory
    receiver = UserFactory

    class Meta:
        model = Notification
        django_get_or_create = ["id"]

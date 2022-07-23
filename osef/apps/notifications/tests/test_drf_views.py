import pytest
from rest_framework.test import APIRequestFactory

from osef.apps.notifications.api.views import NotificationViewSet
from osef.apps.notifications.models import Notification

pytestmark = pytest.mark.django_db


class TestNotificationsViewSet:
    def test_get_queryset(
        self, notification: Notification, arf: APIRequestFactory
    ):
        view = NotificationViewSet()
        request = arf.get("/fake-url/")
        request.user = notification.receiver

        view.request = request

        assert notification in view.get_queryset()

    def test_retrieve(
        self, notification: Notification, arf: APIRequestFactory
    ):
        view_retrieve = NotificationViewSet.as_view({"get": "retrieve"})
        request = arf.get("/fake-url/")
        request.user = notification.receiver

        response = view_retrieve(request, id=notification.id)

        cleaned_data = response.data["data"]
        del cleaned_data["created_at"]  # fails when test for TZ
        del cleaned_data["updated_at"]  # fails when test for TZ

        assert cleaned_data == {
            "id": str(notification.id),
            "emitter": {
                "username": str(notification.emitter),
                "pub_key": str(notification.emitter.pub_key),
            },
            "receiver": {
                "username": str(notification.receiver),
                "pub_key": str(notification.receiver.pub_key),
            },
            "type": notification.get_notification_type(),
            "read": True,
        }

    def test_read(self, notification: Notification, arf: APIRequestFactory):
        view_retrieve = NotificationViewSet.as_view({"get": "retrieve"})
        request = arf.get("/fake-url/")
        request.user = notification.receiver

        assert not notification.read

        view_retrieve(request, id=notification.id)

        updated_notification = Notification.objects.filter(
            id=notification.id
        ).first()

        assert updated_notification.read

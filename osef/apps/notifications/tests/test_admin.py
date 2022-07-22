import pytest
from django.urls import reverse

from osef.apps.notifications.models import Notification
from osef.apps.users.models import User

pytestmark = pytest.mark.django_db


class TestNotificationAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:notifications_notification_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:notifications_notification_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    # noinspection PyShadowingNames
    def test_add(self, admin_client, user1: User, user2: User):
        url = reverse("admin:notifications_notification_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        for notification_type in Notification.NotificationType.values:
            response = admin_client.post(
                url,
                data={
                    "emitter": user1.id,
                    "receiver": user2.id,
                    "type": notification_type,
                },
            )
            assert response.status_code == 302
            assert Notification.objects.filter(
                emitter=user1, receiver=user2
            ).exists()

    # noinspection PyShadowingNames
    def test_view_notification(self, admin_client, notification: Notification):
        url = reverse(
            "admin:notifications_notification_change",
            kwargs={"object_id": notification.pk},
        )
        response = admin_client.get(url)
        assert response.status_code == 200

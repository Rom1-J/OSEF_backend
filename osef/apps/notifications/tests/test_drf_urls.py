import pytest
from django.urls import resolve, reverse

from osef.apps.notifications.models import Notification

pytestmark = pytest.mark.django_db


class TestNotificationAPIUrls:
    def test_notification_detail(self, notification: Notification):
        assert (
            reverse("api:notification-detail", kwargs={"id": notification.id})
            == f"/api/notifications/{notification.id}/"
        )
        assert (
            resolve(f"/api/notifications/{notification.id}/").view_name
            == "api:notification-detail"
        )

    def test_user_list(self):
        assert reverse("api:notification-list") == "/api/notifications/"
        assert (
            resolve("/api/notifications/").view_name == "api:notification-list"
        )

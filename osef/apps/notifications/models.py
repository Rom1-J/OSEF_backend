import uuid

from django.db import models

from osef.apps.users.models import User


class Notification(models.Model):
    class NotificationType(models.TextChoices):
        FILE_RECEIVED = ("F-RCV", "file_received")
        FILE_DOWNLOADED = ("F-DWL", "file_downloaded")
        FILE_REMOVED = ("F-RMV", "file_removed")
        TRANSACTION_RECEIVED = ("T-RCV", "transaction_received")
        TRANSACTION_REMOVED = ("T-RMV", "transaction_removed")
        UNKNOWN = ("UKN", "unknown")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    emitter = models.ForeignKey(
        User,
        verbose_name="Emitter",
        on_delete=models.SET_DEFAULT,
        related_name="notification_emitter",
        default=None,
        blank=True,
    )
    receiver = models.ForeignKey(
        User,
        verbose_name="Receiver",
        on_delete=models.SET_DEFAULT,
        related_name="notification_receiver",
        default=None,
        blank=True,
    )

    type = models.CharField(
        max_length=6,
        choices=NotificationType.choices,
        default=NotificationType.UNKNOWN,
    )

    read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_notification_type(self) -> str:
        return self.NotificationType(self.type).label

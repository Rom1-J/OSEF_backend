import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from osef.apps.users.models import User


class Transaction(models.Model):
    token = models.UUIDField(
        _("Token"), primary_key=True, default=uuid.uuid4, editable=False
    )
    user1 = models.ForeignKey(
        User,
        verbose_name="User 1",
        on_delete=models.SET_DEFAULT,
        related_name="transaction_user1",
        default=None,
        blank=True,
    )
    user2 = models.ForeignKey(
        User,
        verbose_name="User 2",
        on_delete=models.SET_DEFAULT,
        related_name="transaction_user2",
        default=None,
        blank=True,
    )

    accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_file_count(self):
        """Get the number of unread files

        Returns:
            int: number of files
        """
        return self.files.count()

    def __str__(self):
        return "Transaction user1='{}' <-> user2='{}'".format(
            self.user1, self.user2
        )


class File(models.Model):
    id = models.UUIDField(
        _("Identification"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    file = models.FileField(_("File"))
    filename = models.TextField(_("File name"), default="Unknown")
    nonce = models.CharField(_("File nonce"), max_length=255)

    owner = models.ForeignKey(
        User,
        verbose_name="Owner Id",
        on_delete=models.SET_DEFAULT,
        related_name="files_owned",
        default=None,
        blank=True,
    )
    receiver = models.ForeignKey(
        User,
        verbose_name="Receiver Id",
        on_delete=models.SET_DEFAULT,
        related_name="files_received",
        default=None,
        blank=True,
    )

    transaction = models.ForeignKey(
        Transaction,
        verbose_name="Transaction",
        on_delete=models.SET_DEFAULT,
        related_name="files",
        default=None,
        blank=True,
    )

    times_downloaded = models.IntegerField(_("Times Downloaded"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    # =========================================================================

    def save(self, *args, **kwargs):
        self.filename = self.file.name
        self.file.name = str(self.id)

        super().save(*args, **kwargs)

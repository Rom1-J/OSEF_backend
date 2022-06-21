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

    def get_nb_new_files(self):
        """Get the number of unread files

        Returns:
            int: number of files
        """
        return 42


class File(models.Model):
    id = models.UUIDField(
        _("Identification"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    file = models.FileField(_("File"))
    checksum = models.CharField(_("Checksum"), max_length=256)
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

    times_downloaded = models.IntegerField(_("Times Downloaded"), default=0)

    transaction = models.ForeignKey(
        Transaction,
        verbose_name="Transaction",
        on_delete=models.SET_DEFAULT,
        related_name="files",
        default=None,
        blank=True,
    )

    def checksum_match(self, check):
        """Verify if checksum is the same

        Params:
            check:
                str: checksum of the downloaded file before decipher
        Returns:
                bool: True if checksum match, False elsewhere
        """
        return check == self.checksum

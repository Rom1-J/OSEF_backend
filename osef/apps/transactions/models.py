import uuid

from osef.apps.users.models import User
from django.db.models import CharField, UUIDField, FileField, IntegerField, ForeignKey, Model, SET_DEFAULT, SET_NULL
from django.utils.translation import gettext_lazy as _


class Transaction(Model):
    token = UUIDField(_("Token"), primary_key=True, default=uuid.uuid4(), editable=False)
    user1 = ForeignKey(User, verbose_name="User 1", on_delete=SET_DEFAULT, related_name="transactions")
    user2 = ForeignKey(User, verbose_name="User 2", on_delete=SET_DEFAULT, related_name="transactions")
    nb_new_file = IntegerField(_("Number of New Files"), default=0)

    def get_nb_new_files(self):
        """Get the number of unread files

        :return:
            int: number of files
        """
        return self.nb_new_file


class File(Model):
    id = UUIDField(_("Identification"), primary_key=True, default=uuid.uuid4(), editable=False)
    filename = CharField(_("Filename"), max_length=30)
    data = FileField(_("File data"), editable=False)
    checksum = CharField(_("Checksum"), max_length=256)
    owner = ForeignKey(User, verbose_name="Owner Id", on_delete=SET_NULL, related_name="files_owned")
    receiver = ForeignKey(User, verbose_name="Receiver Id", on_delete=SET_NULL, related_name="files_received")
    times_downloaded = IntegerField(_("Times Downloaded"), default=0)
    transaction = ForeignKey(Transaction, verbose_name="Transaction", on_delete=SET_DEFAULT, related_name="files")

    def checksum_match(self, check):
        """Verify if checksum is the same

        :param check:
                str: checksum of the downloaded file before decipher
        :return:
                bool: True if checksum match, False elsewhere
        """
        return check == self.checksum



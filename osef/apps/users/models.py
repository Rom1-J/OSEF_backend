import hashlib
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(
        _("Identification"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    avatar = models.ImageField(_("Avatar"))

    friend_code = models.IntegerField(_("Friend code"), max_length=8)
    pub_key = models.CharField(_("Public Key"))

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse(
            "users:detail",
            kwargs={
                "friend_code": self.friend_code,
            },
        )

    def generate_salt(self):
        """Get unique salt for user's key creation.
        DO NOT STORE IT OR SHARE THE METHOD.

        Returns:
            str: Unique salt for user
        """

        return hashlib.sha256(self.id + self.email).hexdigest()

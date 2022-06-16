import hashlib
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import RandomCharField


class User(AbstractUser):
    id = models.UUIDField(
        _("Identification"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    avatar = models.ImageField(_("Avatar"), default=None, blank=True)

    friend_code = RandomCharField(_("Friend code"), length=10, unique=True)
    pub_key = models.TextField(_("Public Key"), default=None, blank=True)

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

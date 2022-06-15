import datetime
import uuid
import hashlib

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, UUIDField, ImageField, IntegerField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = UUIDField(_("Identification"), primary_key=True, default=uuid.uuid4(), editable=False)
    avatar = ImageField(_("Avatar"))
    last_connection = DateField(_("Last Connection"), default=datetime.date.today)
    friend_code = IntegerField(_("Friend code"), max_length=8)
    pub_key = CharField(_("Public Key"))

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username,
                                               "email": self.email,
                                               "friend_code": self.friend_code,
                                               "avatar_url": self.avatar.url})

    def generate_salt(self):
        """Get unique salt for user's key creation. DO NOT STORE IT OR SHARE THE METHOD.
        :return:
            str: Unique salt for user
        """

        return hashlib.sha256(self.id + self.email).hexdigest()

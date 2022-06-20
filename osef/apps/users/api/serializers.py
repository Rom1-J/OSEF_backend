from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "friend_code",
            "pub_key",
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        }

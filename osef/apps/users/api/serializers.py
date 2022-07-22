from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, read_only=True)
    url = serializers.StringRelatedField(
        source="get_absolute_url", read_only=True
    )

    email = serializers.EmailField(read_only=True)
    friend_code = serializers.CharField(
        min_length=6, max_length=6, read_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "friend_code",
            "pub_key",
            "salt",
            "url",
        ]

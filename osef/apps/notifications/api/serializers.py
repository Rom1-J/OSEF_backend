from rest_framework import serializers

from osef.apps.users.models import User

from ..models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class UserField(serializers.RelatedField):
        @staticmethod
        def to_representation(value: User):
            return {"username": value.username, "pub_key": value.pub_key}

    type = serializers.StringRelatedField(
        source="get_notification_type", read_only=True
    )

    emitter = UserField(read_only=True)
    receiver = UserField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "emitter",
            "receiver",
            "type",
            "read",
            "created_at",
        ]

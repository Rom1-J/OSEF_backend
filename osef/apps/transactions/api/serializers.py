from rest_framework import serializers

from osef.apps.users.models import User

from ..models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    friend_code = serializers.CharField(
        min_length=6, max_length=6, write_only=True
    )

    token = serializers.UUIDField(read_only=True)
    user1 = serializers.StringRelatedField(read_only=True)
    user2 = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ["token", "user1", "user2", "friend_code"]

    def validate(self, data):
        friend_code = data.pop("friend_code")
        data["user1"] = None
        data["user2"] = None

        if (
            user2 := User.objects.filter(friend_code=friend_code).first()
        ) and user2 != self.context["request"].user:
            data["user1"] = self.context["request"].user
            data["user2"] = user2

        return data

from django.db.models import Q
from rest_framework import serializers

from osef.apps.users.models import User

from ..models import File, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class UserField(serializers.RelatedField):
        @staticmethod
        def to_representation(value: User):
            return {"username": value.username, "pub_key": value.pub_key}

    friend_code = serializers.CharField(
        min_length=6, max_length=6, write_only=True
    )

    token = serializers.UUIDField(read_only=True)
    user1 = UserField(read_only=True)
    user2 = UserField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    accepted = serializers.BooleanField(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "token",
            "user1",
            "user2",
            "friend_code",
            "created_at",
            "updated_at",
            "accepted",
        ]

    def validate(self, data):
        friend_code = data.pop("friend_code")
        data["user1"] = None
        data["user2"] = None
        data["accepted"] = None

        if (
            user2 := User.objects.filter(friend_code=friend_code).first()
        ) and user2 != self.context["request"].user:
            user1 = self.context["request"].user
            data["user1"] = user1
            data["user2"] = user2

            transaction = Transaction.objects.filter(
                Q(Q(user1=user1) & Q(user2=user2))
                | Q(Q(user2=user1) & Q(user1=user2))
            ).first()

            data["accepted"] = transaction.accepted if transaction else False

        return data


# =============================================================================
# =============================================================================


class FileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    owner = serializers.StringRelatedField(read_only=True)
    receiver = serializers.StringRelatedField(read_only=True)

    filename = serializers.StringRelatedField(read_only=True)

    times_downloaded = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = File
        fields = [
            "id",
            "file",
            "filename",
            "nonce",
            "owner",
            "receiver",
            "transaction",
            "times_downloaded",
            "created_at",
        ]

    # =========================================================================

    def validate_transaction(self, value: Transaction):
        if (
            self.context["request"].user not in (value.user1, value.user2)
        ) or not value.accepted:
            raise serializers.ValidationError("Unknown transaction.")

        return value

    def validate(self, data):
        owner = self.context["request"].user
        data["owner"] = owner

        transaction = data["transaction"]
        data["receiver"] = (
            transaction.user1
            if owner == transaction.user2
            else transaction.user2
        )

        return data

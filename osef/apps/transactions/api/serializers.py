from rest_framework import serializers

from ..models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["token", "user1", "user2"]

        extra_kwargs = {
            "url": {
                "view_name": "api:transaction-detail",
                "lookup_field": "token",
            }
        }

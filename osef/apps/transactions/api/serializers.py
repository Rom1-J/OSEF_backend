from rest_framework import serializers

from ..models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["token", "user1", "user2"]


class NewTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["token", "user1", "user2"]

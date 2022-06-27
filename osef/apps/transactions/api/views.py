import uuid
from typing import Any

from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Transaction
from .serializers import TransactionSerializer


class TransactionsViewSet(
    RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet
):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, uuid.UUID)  # type: ignore
        return self.queryset.filter(
            Q(user1=self.request.user)  # type: ignore
            | Q(user2=self.request.user)  # type: ignore
        )

    def perform_create(self, serializer: TransactionSerializer):
        user1 = serializer.validated_data["user1"]
        user2 = serializer.validated_data["user2"]

        if user1 and user2:
            serializer.save()

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(
            {"Success": "Transaction pending..."},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )

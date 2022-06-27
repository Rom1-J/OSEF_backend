import uuid
from typing import Any

from django.core.mail import send_mail
from django.db.models import Q
from django.utils.translation import gettext as _
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

        if (user1 and user2) and Transaction.objects.filter(
            Q(Q(user1=user1) & Q(user2=user2))
            | Q(Q(user2=user1) & Q(user1=user2))
        ).count() == 0:
            serializer.save()
            send_mail(
                subject=_("%s asked to connect") % user1.username,
                message=_("Hi %s, please add me to your OSEF network")
                % user1.username,
                from_email="no-reply@osef.net",
                recipient_list=[user2.email],
            )

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(
            {"Success": "Transaction pending..."},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )

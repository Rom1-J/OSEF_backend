import uuid
from typing import Any

from django.core.mail import send_mail
from django.db.models import Q
from django.urls import reverse
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
    lookup_field = "token"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, uuid.UUID)  # type: ignore
        return self.queryset.filter(
            Q(user1=self.request.user)  # type: ignore
            | Q(user2=self.request.user)  # type: ignore
        )

    def perform_create(self, serializer: TransactionSerializer) -> None:
        user1 = serializer.validated_data["user1"]
        user2 = serializer.validated_data["user2"]

        if (user1 and user2) and Transaction.objects.filter(
            Q(Q(user1=user1) & Q(user2=user2))
            | Q(Q(user2=user1) & Q(user1=user2))
        ).count() == 0:
            transaction = serializer.save()

            accept_url = reverse(
                "api:transaction-detail", kwargs={"token": transaction.token}
            )

            send_mail(
                subject=_("%s asked to connect") % user1.username,
                message=_(
                    "Hi %s, please add me to your OSEF network "
                    "<a href='%s'>%s</a>"
                )
                % (user1.username, accept_url, accept_url),
                from_email="no-reply@osef.net",
                recipient_list=[user2.email],
            )

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(
            {"status": "success", "message": "Transaction pending..."},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )

    # =========================================================================

    def retrieve(
        self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        instance: Transaction = self.get_object()

        if (instance.user2 == self.request.user) and not instance.accepted:
            instance.accepted = True
            instance.save()
            send_mail(
                subject=_("%s has accepted to connect")
                % instance.user2.username,
                message=_("Hi %s, %s has just accepted your connection!")
                % (instance.user1.username, instance.user2.username),
                from_email="no-reply@osef.net",
                recipient_list=[instance.user1.email],
            )

            return Response(
                {
                    "status": "success",
                    "message": "Transaction accepted!",
                    "data": {
                        "token": instance.token,
                        "user1": str(instance.user1),
                        "user2": str(instance.user2),
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "status": "success",
                "message": "",
                "data": {
                    "token": instance.token,
                    "user1": str(instance.user1),
                    "user2": str(instance.user2),
                },
            },
            status=status.HTTP_200_OK,
        )

import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from osef.apps.users.models import User

from ..models import Transaction
from .serializers import TransactionSerializer


class TransactionsViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
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

    @action(detail=False, methods=["POST"])
    def new(self, request: WSGIRequest):
        friend_code = request.POST.get("friend_code")

        if user2 := User.objects.filter(friend_code=friend_code).first():
            if Transaction.objects.filter(
                Q(Q(user1=self.request.user) & Q(user2=user2))
                | Q(Q(user2=self.request.user) & Q(user1=user2))
            ):
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={"message": "transaction already exists"},
                )

            transaction = Transaction(user1=request.user, user2=user2)
            transaction.save()

            return Response(
                status=status.HTTP_200_OK,
                data={"message": "transaction created"},
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"message": "transaction not created"},
        )

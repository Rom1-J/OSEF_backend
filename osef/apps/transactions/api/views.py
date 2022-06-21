import uuid

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
            Q(user1__id=self.request.user.id)  # type: ignore
            | Q(user1__id=self.request.user.id)  # type: ignore
        )

    @action(detail=False)
    def new(self, request):
        serializer = TransactionSerializer(
            request.user, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

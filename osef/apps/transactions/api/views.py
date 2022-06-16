from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ..models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)  # type: ignore
        return self.queryset.filter(id=self.request.user.id)  # type: ignore

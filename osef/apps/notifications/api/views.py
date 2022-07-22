import uuid
from typing import Any

from rest_framework import permissions, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, uuid.UUID)  # type: ignore
        return self.queryset.filter(receiver=self.request.user).order_by(
            "-created_at"
        )

    # =========================================================================

    def retrieve(
        self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        instance: Notification = self.get_object()

        instance.read = True
        instance.save()

        return Response(
            {
                "status": "success",
                "message": "",
                "data": NotificationSerializer(instance).data,
            },
            status=status.HTTP_200_OK,
        )

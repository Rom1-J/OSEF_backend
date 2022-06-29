import uuid

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, uuid.UUID)  # type: ignore
        return self.queryset.filter(id=self.request.user.id)  # type: ignore

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["PUT"])
    def pubkey(self, request):
        instance: User = User.objects.filter(id=request.user.id).first()

        pub_key = request.data["pub_key"]
        if pub_key:
            instance.pub_key = pub_key
            instance.save()
            return Response(
                {
                    "status": "success",
                    "message": "pub_key modified",
                    "data": {
                        "pub_key": instance.pub_key,
                        "username": instance.username,
                    },
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": "failed",
                "message": "Wrong key given",
                "data": {
                    "pub_key": pub_key,
                },
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

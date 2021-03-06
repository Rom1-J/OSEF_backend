import pytest
from rest_framework.test import APIRequestFactory

from osef.apps.users.api.views import UserViewSet
from osef.apps.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, arf: APIRequestFactory):
        view = UserViewSet()
        request = arf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, arf: APIRequestFactory):
        view = UserViewSet()
        request = arf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "avatar": user.avatar or None,
            "friend_code": user.friend_code,
            "pub_key": str(user.pub_key),
            "email": user.email,
            "url": f"/api/users/{user.id}/",
            "salt": user.salt(),
        }

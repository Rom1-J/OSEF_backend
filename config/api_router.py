from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from osef.apps.notifications.api.views import NotificationViewSet
from osef.apps.transactions.api.views import FileViewSet, TransactionViewSet
from osef.apps.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("transactions", TransactionViewSet)
router.register("notifications", NotificationViewSet)
router.register("files", FileViewSet)


app_name = "api"
urlpatterns = router.urls

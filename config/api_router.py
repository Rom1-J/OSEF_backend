from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from osef.apps.transactions.api.views import TransactionsViewSet
from osef.apps.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("transactions", TransactionsViewSet)


app_name = "api"
urlpatterns = router.urls

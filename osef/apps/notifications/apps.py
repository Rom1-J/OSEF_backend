from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotificationsConfig(AppConfig):
    name = "osef.apps.notifications"
    verbose_name = _("Notifications")

    def ready(self):
        try:
            import osef.apps.notifications.signals  # noqa F401
        except ImportError:
            pass

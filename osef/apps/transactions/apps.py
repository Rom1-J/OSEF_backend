from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "osef.apps.transactions"
    verbose_name = _("Transactions")

    def ready(self):
        try:
            import osef.apps.transactions.signals  # noqa F401
        except ImportError:
            pass

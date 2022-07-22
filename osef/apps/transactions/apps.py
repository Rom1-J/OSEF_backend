from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionsConfig(AppConfig):
    name = "osef.apps.transactions"
    verbose_name = _("Transactions")

    def ready(self):
        try:
            import osef.apps.transactions.signals  # noqa F401
        except ImportError:
            pass

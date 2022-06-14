from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VueConfig(AppConfig):
    name = "osef.apps.vue"
    verbose_name = _("Vue")

    def ready(self):
        try:
            import osef.apps.vue.signals  # noqa F401
        except ImportError:
            pass

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Notification info"),
            {
                "fields": (
                    "emitter",
                    "receiver",
                    "type",
                    "read",
                )
            },
        ),
    )

    list_display = ["emitter", "receiver", "get_notification_type", "read"]
    search_fields = [
        "id",
        "type",
        "emitter__id",
        "emitter__friend_code",
        "emitter__username",
        "emitter__first_name",
        "emitter__last_name",
        "receiver__id",
        "receiver__friend_code",
        "receiver__username",
        "receiver__first_name",
        "receiver__last_name",
    ]

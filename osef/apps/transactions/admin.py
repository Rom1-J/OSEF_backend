from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import File, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Clients info"),
            {
                "fields": (
                    "user1",
                    "user2",
                )
            },
        ),
    )

    list_display = ["token", "user1", "user2", "get_file_count"]
    search_fields = [
        "token",
        "user1__id",
        "user1__friend_code",
        "user1__username",
        "user1__first_name",
        "user1__last_name",
        "user2__id",
        "user2__friend_code",
        "user2__username",
        "user2__first_name",
        "user2__last_name",
    ]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Global"),
            {"fields": ("file", "transaction")},
        ),
        (
            _("Clients info"),
            {
                "fields": (
                    "owner",
                    "receiver",
                )
            },
        ),
    )

    list_display = ["id", "owner", "receiver"]
    search_fields = [
        "id",
        "owner__id",
        "owner__friend_code",
        "owner__username",
        "owner__first_name",
        "owner__last_name",
        "receiver__id",
        "receiver__friend_code",
        "receiver__username",
        "receiver__first_name",
        "receiver__last_name",
    ]

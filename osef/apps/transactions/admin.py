from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import File, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Global"), {"fields": ("token",)}),
        (
            _("Clients info"),
            {
                "fields": (
                    "user1",
                    "user2",
                )
            },
        ),
        (
            _("Files info"),
            {"fields": ("nb_new_file",)},
        ),
    )

    list_display = ["token", "user1", "user2", "nb_new_file"]
    search_fields = ["token", "user1", "user2"]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Global"),
            {
                "fields": (
                    "id",
                    "file",
                    "checksum",
                )
            },
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
        (
            _("Transactions info"),
            {"fields": ("times_downloaded", "transaction")},
        ),
    )

    list_display = ["id", "checksum", "owner", "receiver"]
    search_fields = ["id", "checksum", "owner"]

# Generated by Django 4.0.6 on 2022-07-22 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('F-RCV', 'file_received'), ('F-DWL', 'file_downloaded'), ('F-RMV', 'file_removed'), ('T-RCV', 'transaction_received'), ('T-RMV', 'transaction_removed'), ('UKN', 'unknown')], default='UKN', max_length=6)),
                ('emitter', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='notification_emitter', to=settings.AUTH_USER_MODEL, verbose_name='Emitter')),
                ('receiver', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='notification_receiver', to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
            ],
        ),
    ]

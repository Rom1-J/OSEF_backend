# Generated by Django 4.0.5 on 2022-06-21 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_transaction_nb_new_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='checksum',
        ),
    ]
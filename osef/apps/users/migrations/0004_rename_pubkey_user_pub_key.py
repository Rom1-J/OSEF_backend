# Generated by Django 4.0.5 on 2022-07-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_pub_key_user_pubkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pubkey',
            new_name='pub_key',
        ),
    ]
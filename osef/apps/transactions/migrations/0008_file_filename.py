# Generated by Django 4.0.5 on 2022-06-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_transaction_modification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.TextField(default='Unknown', verbose_name='File name'),
        ),
    ]

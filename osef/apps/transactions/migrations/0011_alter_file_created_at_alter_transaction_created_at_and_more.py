# Generated by Django 4.0.6 on 2022-07-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_remove_file_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

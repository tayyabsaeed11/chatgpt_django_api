# Generated by Django 5.2 on 2025-05-06 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='api_request_count',
            new_name='daily_count',
        ),
    ]

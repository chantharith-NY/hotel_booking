# Generated by Django 5.1.4 on 2025-01-12 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0014_userprofile_delete_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

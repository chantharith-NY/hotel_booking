# Generated by Django 5.1.4 on 2025-01-14 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0020_room_default_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomimage',
            name='uploaded_at',
        ),
    ]

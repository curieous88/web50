# Generated by Django 5.0.7 on 2024-08-11 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_remove_flight_duration_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Flight',
        ),
    ]

# Generated by Django 4.1 on 2023-02-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='more',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

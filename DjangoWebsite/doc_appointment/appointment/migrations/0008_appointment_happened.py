# Generated by Django 4.1 on 2023-02-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_alter_appointment_booking_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='happened',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1 on 2023-02-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='hour',
            field=models.TimeField(),
        ),
    ]

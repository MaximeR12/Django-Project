# Generated by Django 4.1 on 2023-02-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='booking_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

# Generated by Django 4.1 on 2023-02-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('booking_name', models.CharField(max_length=50)),
            ],
        ),
    ]

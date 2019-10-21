# Generated by Django 2.2.6 on 2019-10-19 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0002_auto_20191018_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='no_of_rooms',
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 4, 15, 10, 508884)),
        ),
    ]
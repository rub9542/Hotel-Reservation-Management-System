# Generated by Django 3.0.2 on 2020-01-28 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hrmsapp', '0015_auto_20200128_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 14, 12, 27, 724352)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 14, 12, 27, 724383)),
        ),
    ]

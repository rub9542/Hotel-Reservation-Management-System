# Generated by Django 2.2.6 on 2019-10-21 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0042_auto_20191021_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 11, 53, 31, 599791)),
        ),
    ]
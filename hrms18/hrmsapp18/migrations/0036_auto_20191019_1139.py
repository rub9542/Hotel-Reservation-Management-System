# Generated by Django 2.2.6 on 2019-10-19 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0035_auto_20191019_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 11, 39, 23, 579037)),
        ),
    ]
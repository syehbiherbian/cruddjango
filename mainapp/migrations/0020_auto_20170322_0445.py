# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 04:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20170322_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 22, 4, 45, 57, 168547)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 4, 45, 57, 169239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 4, 45, 57, 169200, tzinfo=utc)),
        ),
    ]

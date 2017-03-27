# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 02:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20170321_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 22, 2, 15, 38, 230602)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 2, 15, 38, 231351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 2, 15, 38, 231308, tzinfo=utc)),
        ),
    ]

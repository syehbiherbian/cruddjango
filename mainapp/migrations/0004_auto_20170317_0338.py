# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20170317_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 09:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20170327_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 27, 9, 33, 47, 67691)),
        ),
    ]

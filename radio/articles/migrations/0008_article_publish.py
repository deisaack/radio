# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 06:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20170815_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 8, 15, 6, 52, 33, 410305, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

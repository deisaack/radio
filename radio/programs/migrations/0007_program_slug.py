# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0006_auto_20170809_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 00:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0021_auto_20160412_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dateUpdated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 1, 13, 23, 183000), verbose_name=b'event updated date'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 23:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0034_auto_20160412_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dateUpdated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 13, 0, 15, 11, 982000), verbose_name=b'event updated date'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0020_auto_20160412_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dateUpdated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 1, 0, 56, 366000), verbose_name=b'event updated date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='scheduledFlag',
            field=models.TextField(choices=[(1, b'unscheduled'), (2, b'scheduled')], default=1),
        ),
    ]

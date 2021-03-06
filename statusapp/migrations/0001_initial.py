# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=b'', max_length=256)),
                ('dateStart', models.DateTimeField(verbose_name=b'event start date')),
                ('dateEnd', models.DateTimeField(verbose_name=b'event end date')),
                ('dateUpdated', models.DateTimeField(default=datetime.datetime(2016, 4, 14, 2, 13, 54, 509000), verbose_name=b'event updated date')),
                ('resolvedFlag', models.IntegerField(choices=[(1, b'resolved'), (2, b'outstanding')], default=2)),
                ('status', models.IntegerField(choices=[(1, b'normal'), (2, b'critical')], default=1)),
                ('scheduleFlag', models.IntegerField(choices=[(2, b'scheduled'), (1, b'unscheduled')], default=1)),
            ],
        ),
    ]

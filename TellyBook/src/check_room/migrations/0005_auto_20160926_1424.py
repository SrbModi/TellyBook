# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-26 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_room', '0004_remove_rooms_wpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='check_rooms',
            name='etime',
            field=models.TimeField(default='01:00', null=True),
        ),
        migrations.AddField(
            model_name='check_rooms',
            name='stime',
            field=models.TimeField(default='01:00', null=True),
        ),
    ]

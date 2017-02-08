# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_room', '0005_auto_20160926_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='name',
        ),
        migrations.AddField(
            model_name='booked',
            name='desc',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booked',
            name='eventname',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booked',
            name='eventroom',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
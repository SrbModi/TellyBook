# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_room', '0008_booked_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_rooms',
            name='userid',
            field=models.SmallIntegerField(null=True),
        ),
    ]

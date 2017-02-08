# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('stime', models.TimeField()),
                ('etime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='check_rooms2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.SmallIntegerField()),
                ('capacity', models.SmallIntegerField()),
                ('date', models.DateField()),
                ('stime', models.TimeField(default='01:00', null=True)),
                ('etime', models.TimeField(default='01:00', null=True)),
                ('proom', models.CharField(max_length=120)),
                ('floor', models.SmallIntegerField()),
                ('mike', models.SmallIntegerField()),
                ('stage', models.SmallIntegerField()),
                ('projector', models.SmallIntegerField()),
            ],
        ),
    ]
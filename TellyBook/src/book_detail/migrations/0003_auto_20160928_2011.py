# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_detail', '0002_book_detail_bdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proid', models.SmallIntegerField()),
                ('userid', models.SmallIntegerField()),
                ('reqid', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='n',
            field=models.SmallIntegerField(default=1),
        ),
    ]

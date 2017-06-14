# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 08:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='video/%Y/%m/')),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('video_url', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
            ],
        ),
    ]

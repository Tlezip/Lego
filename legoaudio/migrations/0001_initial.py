# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='audio/%Y/%m/')),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('audio_url', models.CharField(default='', max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

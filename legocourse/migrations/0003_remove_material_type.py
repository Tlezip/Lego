# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legocourse', '0002_auto_20170616_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='type',
        ),
    ]
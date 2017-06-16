# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legotest', '0007_auto_20170616_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='Question',
        ),
        migrations.AddField(
            model_name='question',
            name='sectionid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legotest.Section'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legotest', '0004_auto_20170615_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='condition',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='descripe',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='max_submit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='overview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='provider',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

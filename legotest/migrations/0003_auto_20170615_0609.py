# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legotest', '0002_auto_20170615_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
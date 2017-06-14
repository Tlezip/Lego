# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legotest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='sectionNum',
        ),
        migrations.RemoveField(
            model_name='section',
            name='typequestion',
        ),
        migrations.RemoveField(
            model_name='test',
            name='sectionID',
        ),
        migrations.AddField(
            model_name='section',
            name='testid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='legotest.Test'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

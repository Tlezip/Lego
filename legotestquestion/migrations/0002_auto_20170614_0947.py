# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legotestquestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_isrequire',
            new_name='is_require',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_num_show',
            new_name='num_show',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='questions',
        ),
        migrations.AddField(
            model_name='bank',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legotestquestion.Bank'),
        ),
    ]
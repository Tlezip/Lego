# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.IntegerField(choices=[(0, 'Multiple Choice'), (1, 'Fill Description'), (2, 'Fill the Box'), (3, 'Match')], default=0)),
                ('answer', models.CharField(max_length=50)),
                ('num_show', models.IntegerField()),
                ('is_require', models.IntegerField(default=0)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legotestquestion.Bank')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='questionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legotestquestion.Question'),
        ),
    ]

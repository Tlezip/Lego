# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legotestquestion', '0002_auto_20170614_0947'),
        ('legotest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typecondition', models.IntegerField(choices=[(0, 'random'), (1, 'choose')])),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legotestquestion.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionid', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='section',
            old_name='fullscore',
            new_name='full_score',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='sectionNum',
            new_name='num',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='testid',
            new_name='test',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='Img_name',
            new_name='image',
        ),
        migrations.AddField(
            model_name='section',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='section',
            name='pull',
            field=models.IntegerField(choices=[(0, 'Basic'), (1, 'Bank')], default=0),
        ),
        migrations.AddField(
            model_name='condition',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legotest.Section'),
        ),
    ]

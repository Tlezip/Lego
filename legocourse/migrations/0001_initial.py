# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course/%Y/%m/')),
                ('overview', models.TextField(blank=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True)),
                ('is_display', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.PositiveSmallIntegerField(choices=[(5, 'Scorm'), (6, 'File Upload'), (3, 'Test'), (4, 'Audio'), (1, 'Web Link'), (0, 'Video'), (2, 'Document')], default=0)),
                ('sort', models.IntegerField(db_index=True, default=1)),
                ('object_id', models.PositiveSmallIntegerField(default=1)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sort', models.IntegerField(db_index=True, default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='legocourse.Course')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='legocourse.Section'),
        ),
    ]

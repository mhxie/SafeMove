# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-06 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=30)),
                ('phone_number', models.TextField(default='', max_length=15)),
                ('age', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('event_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VisualData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('tag', models.IntegerField(default=0)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemadatabase', '0002_auto_20180112_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='category',
        ),
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(to='cinemadatabase.Category'),
        ),
    ]

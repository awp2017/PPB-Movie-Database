# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemadatabase', '0005_auto_20180113_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id_discussion',
            new_name='discussion',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='discussion',
            old_name='id_film',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='discussion',
            old_name='id_user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.FileField(default='/media/sample.jpg', upload_to='actors'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.FileField(default='/media/sample.jpg', upload_to='films'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-01 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0013_auto_20190301_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/default.png', upload_to='static/images/uploads'),
        ),
    ]
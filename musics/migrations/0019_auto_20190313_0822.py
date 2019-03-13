# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 08:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0018_auto_20190311_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/default.png', upload_to='static/images/uploads', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
        ),
    ]

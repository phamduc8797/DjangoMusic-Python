# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useractions', '0005_lyric_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='accept',
            field=models.BooleanField(default=True),
        ),
    ]

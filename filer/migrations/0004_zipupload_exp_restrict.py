# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-13 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0003_auto_20160711_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='zipupload',
            name='exp_restrict',
            field=models.BooleanField(default=False),
        ),
    ]

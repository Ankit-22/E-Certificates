# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-22 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20180122_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_url',
            field=models.CharField(max_length=1000),
        ),
    ]
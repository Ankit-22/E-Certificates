# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-22 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=600)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=255)),
                ('event_name', models.CharField(max_length=255)),
                ('attendees', models.ManyToManyField(to='creator.Attendee')),
            ],
        ),
    ]

# Generated by Django 2.0.4 on 2018-04-30 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20180430_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='division',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='year_of_study',
        ),
    ]

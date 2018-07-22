# Generated by Django 2.0.4 on 2018-04-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20180430_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='division',
            field=models.CharField(default='A', max_length=255),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='year_of_study',
            field=models.CharField(choices=[('TY', 'Third Year'), ('SY', 'Second Year'), ('FY', 'First Year'), ('B.Tech', 'Final/Fourth Year')], default='FY', max_length=255),
        ),
    ]
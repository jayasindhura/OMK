# Generated by Django 3.0.3 on 2020-02-22 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0013_auto_20200222_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session_schedule',
            name='session_date',
        ),
    ]

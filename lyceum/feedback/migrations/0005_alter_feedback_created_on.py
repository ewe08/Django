# Generated by Django 3.2.16 on 2022-12-05 12:40

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 15, 40, 9, 922365)),
        ),
    ]

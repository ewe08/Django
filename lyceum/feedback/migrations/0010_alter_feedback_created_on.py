# Generated by Django 3.2.16 on 2022-12-07 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_alter_feedback_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 22, 45, 20, 413068)),
        ),
    ]
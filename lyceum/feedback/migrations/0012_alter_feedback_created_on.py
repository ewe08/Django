# Generated by Django 3.2.16 on 2022-12-08 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0011_auto_20221208_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 18, 19, 28, 244099)),
        ),
    ]

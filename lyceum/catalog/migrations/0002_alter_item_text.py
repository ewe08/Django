# Generated by Django 3.2.16 on 2022-10-31 15:26

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_must_be_param]),
        ),
    ]

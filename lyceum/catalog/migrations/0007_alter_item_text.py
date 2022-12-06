# Generated by Django 3.2.16 on 2022-12-06 15:25

import catalog.validators
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=tinymce.models.HTMLField(help_text='Описание предмета. Должны быть слова "превосходно" или "роскошно".', validators=[catalog.validators.validate_must_be_param], verbose_name='описание'),
        ),
    ]

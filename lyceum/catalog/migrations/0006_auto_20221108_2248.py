# Generated by Django 3.2.16 on 2022-11-08 15:48

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20221108_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Описание предмета. Должны быть слова "превосходно" или "роскошно".', validators=[catalog.validators.validate_must_be_param], verbose_name='описание'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m')),
                ('item', models.ForeignKey(help_text='Предмет. Связь o2m.', on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='предмет')),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]

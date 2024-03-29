# Generated by Django 3.2.16 on 2022-11-30 04:16

import django.core.validators
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models

import catalog.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, help_text='Проверка на публикацю.', verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Название.', max_length=150, verbose_name='название')),
                ('slug', models.SlugField(help_text='slug для будущей ссылки.', max_length=200, unique=True)),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Вес, должен быть 0 до 32767.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(32767)], verbose_name='вес')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, help_text='Проверка на публикацю.', verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Название.', max_length=150, verbose_name='название')),
                ('text', tinymce.models.HTMLField(help_text='Описание предмета. Должны быть слова "превосходно" или "роскошно".', validators=[catalog.validators.validate_must_be_param], verbose_name='описание')),
                ('is_on_main', models.BooleanField(default=False, verbose_name='В главной?')),
                ('category', models.ForeignKey(help_text='Категория. Связь o2m.', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, help_text='Проверка на публикацю.', verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Название.', max_length=150, verbose_name='название')),
                ('slug', models.SlugField(help_text='slug для будущей ссылки.', max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m', verbose_name='изображение')),
                ('item_galery', models.ForeignKey(blank=True, help_text='фотографии предмета.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_galery', to='catalog.item', verbose_name='галерея фотографий')),
                ('item_main', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фотографии',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(help_text='теги. Связь m2m.', to='catalog.Tag', verbose_name='тэги'),
        ),
    ]

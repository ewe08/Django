# Generated by Django 3.2.16 on 2022-10-31 14:36

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('weight', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('text', models.TextField(validators=[catalog.validators.validate_must_be_param])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('tags', models.ManyToManyField(to='catalog.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

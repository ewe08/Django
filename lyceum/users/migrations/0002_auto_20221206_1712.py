# Generated by Django 3.2.16 on 2022-12-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, help_text='Дата в формате дд.мм.гггг', null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(help_text='Ваш email', max_length=254, unique=True, verbose_name='email'),
        ),
    ]
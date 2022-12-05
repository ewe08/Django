# Generated by Django 3.2.16 on 2022-12-05 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_alter_item_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[(1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')], max_length=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'рейтинг',
                'verbose_name_plural': 'рейтинги',
            },
        ),
    ]

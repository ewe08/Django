from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class Tag(AbstractModelWithSlug):
    class Meta:
        verbose_name_plural = 'Тэги'


class Category(AbstractModelWithSlug):
    weight = models.PositiveSmallIntegerField(
            'вес',
            default=100,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(32767)
            ],
            help_text='Вес, должен быть 0 до 32767.'
    )

    class Meta:
        verbose_name_plural = 'категории'


class Item(AbstractModel):
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.CASCADE,
        help_text='Категория. Связь o2m.'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='тэги',
        help_text='теги. Связь m2m.'
    )
    text = models.TextField(
        'описание',
        validators=[
            validate_must_be_param('превосходно', 'роскошно')],
        help_text='Описание предмета. Должны быть слова "превосходно"'
                  ' или "роскошно".'
    )

    class Meta:
        verbose_name_plural = 'Товары'

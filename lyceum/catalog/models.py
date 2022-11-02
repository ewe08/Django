from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class Tag(AbstractModelWithSlug):
    class Meta:
        verbose_name_plural = 'Тэги'


class Category(AbstractModelWithSlug):
    weight = models.PositiveSmallIntegerField('Вес', default=100,
                                              validators=[
                                                MinValueValidator(1),
                                                MaxValueValidator(32766)],
                                              help_text='Вес, должен быть > 0'
                                                        ' и < 32767.')

    class Meta:
        verbose_name_plural = 'Категории'


class Item(AbstractModel):
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 help_text='Категория. Связь o2m.')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги',
                                  help_text='Теги. Связь m2m.')
    text = models.TextField('Описание', validators=[
        validate_must_be_param('превосходно', 'роскошно')],
        help_text='Описание предмета. Должны быть слова "превосходно"'
                  ' или "роскошно".')

    class Meta:
        verbose_name_plural = 'Товары'

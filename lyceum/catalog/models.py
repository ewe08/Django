from django.db import models

from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class Tag(AbstractModelWithSlug):

    class Meta:
        verbose_name_plural = 'Тэги'


class Category(AbstractModelWithSlug):
    weight = models.PositiveSmallIntegerField('Вес', default=100)

    class Meta:
        verbose_name_plural = 'Категории'


class Item(AbstractModel):
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    text = models.TextField('Описание', validators=[
        validate_must_be_param('превосходно', 'роскошно')],
        help_text='Описание')

    class Meta:
        verbose_name_plural = 'Товары'

from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField

from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class Tag(AbstractModelWithSlug):
    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


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
        verbose_name = 'категория'
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
    text = HTMLField(
        'описание',
        validators=[
            validate_must_be_param('превосходно', 'роскошно')],
        help_text='Описание предмета. Должны быть слова "превосходно"'
                  ' или "роскошно".',
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    upload = models.ImageField(
        upload_to='uploads/%Y/%m',
        blank=True,
        null=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m')
    item = models.ForeignKey(
        Item,
        verbose_name='предмет',
        on_delete=models.CASCADE,
        help_text='Предмет. Связь o2m.')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField

from .managers import ItemManager
from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class TagManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .only('name')
        )


class Tag(AbstractModelWithSlug):
    objects = TagManager()

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
            help_text='Вес, должен быть от 0 до 32767.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Item(AbstractModel):
    objects = ItemManager()

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
    is_on_main = models.BooleanField(
        'На главной?',
        default=False,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Photo(models.Model):
    image = models.ImageField(
        'изображение',
        upload_to='uploads/%Y/%m'
    )

    item_main = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    item_galery = models.ForeignKey(
        Item,
        verbose_name='галерея фотографий',
        on_delete=models.CASCADE,
        help_text='фотографии предмета.',
        related_name='item_galery',
        null=True,
        blank=True
    )

    @property
    def get_img(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

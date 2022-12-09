from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField

from .managers import ItemManager, TagManager
from .validators import validate_must_be_param
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel


class Tag(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    """Tag model with name, is_published and slug field."""
    objects = TagManager()

    name = models.CharField(
        'название',
        max_length=150,
        unique=True,
        help_text='Название.',
    )

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
        unique_together = (NamedBaseModel.name.field.name,)


class Category(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    """Category model with name, is_published, slug and weight field."""
    weight = models.PositiveSmallIntegerField(
            'вес',
            default=100,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(32767),
            ],
            help_text='Вес, должен быть от 0 до 32767.',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        unique_together = (NamedBaseModel.name.field.name,)


class Item(NamedBaseModel, PublishedBaseModel):
    """
    Item model with name, is_published, category,
    tags, text and is_on_main field.
    """
    objects = ItemManager()
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.CASCADE,
        help_text='Категория. Связь o2m.',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='тэги',
        help_text='Теги. Связь m2m.',
    )
    text = HTMLField(
        'описание',
        validators=[
            validate_must_be_param('превосходно', 'роскошно'),
        ],
        help_text='Описание предмета. Должны быть слова "превосходно" '
                  'или "роскошно".',
    )
    is_on_main = models.BooleanField(
        'на главной?',
        default=False,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)
        default_related_name = 'items'


class Photo(models.Model):
    """Photo model with image, main_item and item_gallery field."""

    image = models.ImageField(
        'изображение',
        upload_to='uploads/%Y/%m',
    )

    item_main = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='main_photos',
    )

    item_galery = models.ForeignKey(
        Item,
        verbose_name='галерея фотографий',
        on_delete=models.CASCADE,
        help_text='Фотографии предмета.',
        related_name='photos',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

    def __str__(self):
        return self.image.name

    @property
    def get_img(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
            )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">',
                )
        return None

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField(
        'название',
        max_length=150,
        help_text='Название.'
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
        help_text='Проверка на публикацю.'
    )

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='slug для будущей ссылки.'
    )

    class Meta:
        abstract = True

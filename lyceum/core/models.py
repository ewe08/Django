from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField(
        'название',
        max_length=150,
        help_text='Название.'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class UniqueNamedBaseModel(models.Model):
    name = models.CharField(
        'название',
        unique=True,
        max_length=150,
        help_text='Название.',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
        help_text='Проверка на публикацию.',
    )

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Slug для будущей ссылки.',
    )

    class Meta:
        abstract = True

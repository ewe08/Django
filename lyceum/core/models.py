from django.db import models


# Абстрактные классы для будущего наследования


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
        help_text='Проверка на публикацю.'
    )

    name = models.CharField(
        'название',
        max_length=150,
        help_text='Название.'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractModelWithSlug(AbstractModel):
    name = models.CharField(
        'название',
        max_length=150,
        help_text='Название.',
        unique=True
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Slug для будущей ссылки.'
    )

    class Meta:
        abstract = True

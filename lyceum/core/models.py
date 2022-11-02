from django.db import models

# Абстрактные классы для будущего наследования


class AbstractModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True,
                                       help_text='Проверка на публикацю.')
    name = models.CharField('Название', max_length=150,
                            help_text='Название.')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractModelWithSlug(AbstractModel):
    slug = models.SlugField(max_length=200, unique=True,
                            help_text='slug для будущей ссылки.')

    class Meta:
        abstract = True

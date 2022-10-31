from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractModelWithSlug(AbstractModel):
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        abstract = True

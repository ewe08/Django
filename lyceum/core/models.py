from django.db import models


class AbstractModel(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractModelWithSlug(AbstractModel):
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        abstract = True

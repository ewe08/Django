from django.db import models

from .validators import validate_must_be_param
from core.models import AbstractModel, AbstractModelWithSlug


class Tag(AbstractModelWithSlug):
    pass


class Category(AbstractModelWithSlug):
    weight = models.PositiveSmallIntegerField(default=100)


class Item(AbstractModel):
    text = models.TextField(validators=[validate_must_be_param])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

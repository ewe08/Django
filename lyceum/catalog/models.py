from django.db import models
from .validators import validate_must_be_param


class Tag(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    weight = models.PositiveSmallIntegerField(default=100)
    slug = models.SlugField(max_length=200, unique=True)


class Item(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    text = models.TextField(validators=[validate_must_be_param])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, on_delete=models.CASCADE)

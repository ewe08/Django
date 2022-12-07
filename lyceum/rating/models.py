from django.db import models
from django.db.models import UniqueConstraint

from catalog.models import Item
from users.models import CustomUser


class Rating(models.Model):
    choices = [
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    ]

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item'
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user'
    )

    rate = models.CharField(
        max_length=1,
        choices=choices,
    )

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'
        constraints = [
            UniqueConstraint(fields=['user', 'rate'], name='rating_once')
        ]

    def __str__(self):
        return f'{self.rate} - {self.item.name} - {self.user.email}'

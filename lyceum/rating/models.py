from django.db import models
from django.db.models import UniqueConstraint

from catalog.models import Item
from users.models import CustomUser


class RainitgStatus(models.IntegerChoices):
    HATE = 1, 'Ненависть'
    DISLIKE = 2, 'Неприязнь'
    NEUTRAL = 3, 'Нейтрально'
    ADORING = 4, 'Обожание'
    LOVE = 5, 'Любовь'


class Rating(models.Model):
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

    rate = models.IntegerField(
        choices=RainitgStatus.choices
    )

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'
        constraints = [
            UniqueConstraint(fields=['user', 'rate'], name='rating_once')
        ]

    def __str__(self):
        return f'{self.rate} - {self.item.name} - {self.user.email}'

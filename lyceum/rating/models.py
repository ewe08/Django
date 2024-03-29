from django.db import models
from django.db.models import UniqueConstraint

from catalog.models import Item
from users.models import CustomUser


class RanitgStatus(models.IntegerChoices):
    """Class with rating statuses."""

    HATE = 1, 'Ненависть'
    DISLIKE = 2, 'Неприязнь'
    NEUTRAL = 3, 'Нейтрально'
    ADORING = 4, 'Обожание'
    LOVE = 5, 'Любовь'


class Rating(models.Model):
    """Rating model with item, user and rate field."""

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        help_text='Предмет оценки.'
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text='Оценщик товара.'
    )

    rate = models.IntegerField(
        choices=RanitgStatus.choices,
        help_text='Оценка товара.'
    )

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'
        constraints = [
            UniqueConstraint(
                fields=['user', 'rate'],
                name='rating_once',
            )
        ]
        default_related_name = 'ratings'

    def __str__(self):
        return f'{self.rate} - {self.item.name} - {self.user.email}'

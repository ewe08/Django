from datetime import datetime

from django.db import models


class Feedback(models.Model):
    """Feedback model with text and creation data field."""

    text = models.TextField(
        help_text='Сюды текст надо для письма'
    )
    created_on = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обатные связи'

    def __str__(self):
        return str(self.created_on)

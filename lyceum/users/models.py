from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        'email',
        unique=True,
        help_text='Ваш email'
    )
    birthday = models.DateField(
        'день рождения',
        null=True,
        blank=True,
        help_text='Дата в формате дд.мм.гггг'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


def user_avatar_upload_to(instance, filename):
    return f'users/{instance.pk or "new"}/{filename}'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(
        upload_to=user_avatar_upload_to,
        verbose_name='Аватар',
        blank=True,
        null=True,
        help_text='Загрузите свой аватар',
    )
    phone = models.CharField(
        max_length=32,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона',
    )
    country = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name='Страна',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите email')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE, help_text='Введите страну')

    token = models.CharField(max_length=50, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.email}"

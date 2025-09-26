from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    is_active = models.BooleanField(default=True, verbose_name="Активный сотрудник")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

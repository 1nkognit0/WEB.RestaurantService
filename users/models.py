from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [
        ('admin', 'Админ'),
        ('waiter', 'Официант'),
        ('chef', 'Повар'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f'Пользователь {self.username}({self.role})'

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    cccd = models.CharField(max_length=12, unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'cccd'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.cccd

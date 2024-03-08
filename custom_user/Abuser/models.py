from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class cuser(AbstractUser):
    username = None
    Phone = models.CharField(max_length=11, unique=True, default='null')
    user_profile = models.ImageField(upload_to="profile", default='null')

    USERNAME_FIELD = 'Phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.Phone

from django.contrib.auth.models import AbstractUser
from django.db import models

#customer user
class User(AbstractUser):
    avatar = models.CharField(max_length=200)

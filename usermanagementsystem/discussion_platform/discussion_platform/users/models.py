

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

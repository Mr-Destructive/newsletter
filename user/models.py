from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    gapps_key = models.CharField(max_length=16, default='')

    REQUIRED_FIELDS = ['gapps_key', 'email']


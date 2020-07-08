from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    passport_number = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.CharField(max_length=40, blank=True, null=True)
    nationality = models.CharField(max_length=40, blank=True, null=True)

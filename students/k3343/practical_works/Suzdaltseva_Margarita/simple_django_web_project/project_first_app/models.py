from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

class Car(models.Model):
    trademark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    cars = models.ManyToManyField(Car, through='Ownership')
    passport = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

class DriversLicense(models.Model):
    TYPES = (
        ('A','moto'),
        ('B','autoB'),
        ('C','autoC'),
        ('D', 'autoD'),
        ('E', 'autoE'),
        # и так далее
    )
    number = models.CharField(max_length=50)
    date_given = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


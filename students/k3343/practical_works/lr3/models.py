from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField()
    passport = models.CharField(max_length=128, blank=True, null=True, unique=True)
    nationality = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.username

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    gos_num = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

    def __str__(self):
        return self.gos_num

class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class License(models.Model):
    TYPE_LICENSE = (
        ('A1', 'A'),
        ('B1', 'B'),
        ('C1', 'C'),
        ('D1', 'D'),
        ('E1', 'E'),
        ('T1', 'Tm'),
        ('T2', 'Tb'),
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_date = models.DateField()
    type = models.CharField(max_length=128)
    license = models.CharField(max_length=128)

    def __str__(self):
        return self.license
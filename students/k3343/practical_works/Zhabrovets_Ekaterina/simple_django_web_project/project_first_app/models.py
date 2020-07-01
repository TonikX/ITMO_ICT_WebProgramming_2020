from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Owner(AbstractUser):
    email = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


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
    license_number = models.CharField(max_length=6)
    begin_date = models.DateField()
    type = models.CharField(max_length=3, choices=TYPE_LICENSE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_number


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    own = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

    def __str__(self):
        return self.number


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

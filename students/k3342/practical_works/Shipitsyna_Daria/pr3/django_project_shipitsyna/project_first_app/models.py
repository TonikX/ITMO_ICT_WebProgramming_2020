from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Car(models.Model):
    mark = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    gov_number = models.CharField(max_length=128)

class Owner(AbstractUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(default='1999-01-01', blank=True, null=True)
    own_car = models.ManyToManyField(Car, through='Ownership')
    passport = models.IntegerField(default=1234567890, null=True)
    address = models.CharField(max_length=150, default='russia', blank=True, null=True)
    nationality = models.CharField(max_length=30, default='secret', blank=True, null=True)

class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Driver_license(models.Model):
    license_number = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    TYPE_LICENSE =(
        ('A', 'MOTO'),
        ('B', 'CAR'),
        ('C', 'TRUNK'),
        ('D', 'BUS'),
        ('M', 'MOPED'),
    )
    type = models.CharField(max_length=2, choices=TYPE_LICENSE)

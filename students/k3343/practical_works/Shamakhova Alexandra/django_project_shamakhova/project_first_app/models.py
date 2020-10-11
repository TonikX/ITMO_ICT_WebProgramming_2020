from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Car(models.Model):
    car_maker = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_colour = models.CharField(max_length=30)
    car_number = models.CharField(max_length=6)


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(default='1975-05-05')
    cars = models.ManyToManyField(Car, through='Ownership')
    passport = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    ethnicity = models.CharField(max_length=30, blank=True, null=True)


class Ownership(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_date = models.DateField()
    last_date = models.DateField()


class DriverLicense(models.Model):
    LIC_TYPES = (
        ('A', 'motorcycle'),
        ('B', 'automobile'),
        ('C', 'truck'),
        ('D', 'bus')
    )
    lic_number = models.PositiveIntegerField()
    lic_issue_date = models.DateField()
    lic_type = models.CharField(max_length=1, choices=LIC_TYPES)
    lic_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

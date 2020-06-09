from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.conf import settings


class Car(models.Model):
    producer = models.CharField(max_length=40)
    model = models.CharField(max_length=25)
    color = models.CharField(max_length=40)
    state_num = models.CharField(max_length=17)


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    passport_data = models.CharField(max_length=10, null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)
    nationality = models.CharField(max_length=40, null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Ownership')


class DrivingLicense(models.Model):
    DLType = (
        ('AA1M', 'aa1m'),
        ('BB1M', 'bb1m'),
        ('BB1CC1M', 'bb1cc1m'))
    license_num = models.CharField(max_length=10)
    issue_date = models.DateField()
    type = models.CharField(choices=DLType, max_length=7)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    own_starting_date = models.DateField()
    own_expiring_date = models.DateField()

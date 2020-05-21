from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    colour = models.CharField(max_length=20)
    number = models.IntegerField()


class Owner(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField(default="2000-01-01")
    passsport = models.CharField(max_length=10, default="default")
    address = models.CharField(max_length=100, null=True)
    nation = models.CharField(max_length=100, null=True)
    car = models.ManyToManyField(Car, through='Owning')


class Owning(models.Model):
    own_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Passport(models.Model):
    TYPE_EX = (
        ('B', 'Van'),
        ('A', 'Motorbike'),
        ('C', 'SmallCar'),
    )
    own_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.IntegerField
    start_date = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_EX)

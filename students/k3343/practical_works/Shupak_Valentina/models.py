from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
#1
#class Owner(models.Model):
 #   first_name = models.CharField(max_length=50)
  #  last_name = models.CharField(max_length=50)
   # birth_date = models.DateField()


class Car(models.Model):
    mark_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    owners = models.ManyToManyField(Owner, through='Owning')
# 3
class Owner(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default='1900-01-01')
    passport = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    car = models.ManyToManyField(Car, through='Owning')

class Owning(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class License(models.Model):
    License_Type = (
        ('A', 'Motorcycle'),
        ('B', 'Passenger car'),
        ('C', 'Commercial vehicle'),
        ('D', 'Bus'),
        ('BE', 'Passenger car with a trailer'),
        ('CE', 'Truck with a trailer'),
        ('DE', 'Bus with a trailer'),
        ('Tm', 'Tram'),
        ('Tb', 'Trolleybus'),
    )
    license_number = models.CharField(max_length=10)
    starting_date = models.DateField()
    type = models.CharField(max_length=10, choices=License_Type)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

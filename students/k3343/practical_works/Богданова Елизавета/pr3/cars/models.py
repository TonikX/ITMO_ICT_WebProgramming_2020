from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    id_car = models.CharField(max_length=50, primary_key=True)

class User(AbstractUser):
    passport = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Owning')

    def __str__(self):
        car_owner = "%s %s" % (self.first_name, self.last_name)
        return car_owner


class Driver_license(models.Model):
    id_license = models.CharField(max_length=50, primary_key=True)
    date_of_issue = models.DateField()
    CategoryType = models.TextChoices('CategoryType','A B C')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=1)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class Owning(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_start_owning = models.DateField()
    date_of_end_owning = models.DateField()
from django.db import models

# Create your models here.

class CarOwner(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    date_of_birth = models.DateField()

class Car(models.Model):
    car_make = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    number_plate = models.CharField(max_length=128)
    car_owner = models.ManyToManyField(CarOwner, through='Ownership')

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class DriversLicense(models.Model):
    TYPE_LICENSE = (
        ('A', 'Motorcycle'),
        ('B', 'Car'),
        ('C', 'Truck'),
    )
    driver_license_number = models.CharField(max_length=128)
    date_of_issue = models.DateField()
    license_type = models.CharField(max_length=1, choices=TYPE_LICENSE)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

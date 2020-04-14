from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()

class DrivingLicense(models.Model):
    owner_dl = models.ForeignKey(Owner,on_delete=models.CASCADE)
    license_number = models.IntegerField()
    receiving_date = models.DateField()
    TYPE_DL =  [
        ('A', 'license_A'),
        ('B', 'license_B'),
        ('C', 'license_C'),
        ('D', 'license_D'),
        ('E', 'license_E')
    ]
    type = models.CharField(max_length=2, choices=TYPE_DL)


class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gov_number = models.CharField(max_length=50)


class Ownership(models.Model):
    owner_car = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


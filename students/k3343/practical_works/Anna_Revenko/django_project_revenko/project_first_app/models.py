from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField()

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    gos_num = models.ManyToManyField(Owner, through='Ownership')

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    is_date = models.DateField()
    type = models.CharField(max_length=128)
    license = models.CharField(max_length=128)
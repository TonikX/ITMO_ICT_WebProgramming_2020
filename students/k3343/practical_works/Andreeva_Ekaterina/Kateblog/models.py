from django.db import models


# Create your models here.

class Owner(models.Model):
    Owner_name = models.CharField(primary_key=True, max_length=50)
    Surname = models.CharField(max_length=50)
    Date_of_birth = models.DateField()


class Udostoverenie(models.Model):
    Number = models.CharField(max_length=50, primary_key=True)
    Date = models.DateField()
    Type = models.CharField(max_length=50)
    Owner_names = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Auto(models.Model):
    Marka = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Colour = models.CharField(max_length=50)
    Auto_number = models.CharField(primary_key=True, max_length=50)


class Ownship(models.Model):
    Date_end = models.DateField()
    Date_start = models.DateField()
    Owner_n = models.ForeignKey(Owner, on_delete=models.CASCADE)
    Auto_number = models.ForeignKey(Auto, on_delete=models.CASCADE)

from django.db import models
from django.utils import timezone
import datetime

class Person(models.Model):
    def __str__(self):
        return self.name + " " + self.second_name

    name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    date = models.DateField()

class DriverLicence(models.Model):
    def __str__(self):
        return self.number

    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )

    TYPE = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
    )

    number = models.CharField(max_length=128)
    date = models.DateField()
    type = models.PositiveSmallIntegerField(
        choices=TYPE,
        default=1
    )


class Ownership(models.Model):


    owner = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )

    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
    )

    start_date = models.DateField()
    end_date = models.DateField()


class Vehicle(models.Model):
    def __str__(self):
        return self.manufacturer + " " + self.model + "(" + self.vehicle_number + ")"

    manufacturer = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    vehicle_number = models.CharField(max_length=128)
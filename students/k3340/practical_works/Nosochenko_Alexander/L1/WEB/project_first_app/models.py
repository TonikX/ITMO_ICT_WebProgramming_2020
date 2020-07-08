from django.db import models
from datetime import datetime

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    vehicle_number = models.CharField(max_length=10)

class Person(models.Model):
    def __str__(self):
        return self.name + " " + self.surname

    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    bdate = models.DateField

    vehicle = models.ManyToManyField(Vehicle, through='Ownership')

class Driver_License(models.Model):

    TYPE = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    ID_number = models.IntegerField()
    date_of_issue = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=TYPE,
        default="A"
    )
    owner = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.ID_number)


class Ownership(models.Model):
    owner = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
    )
    start_date_of_ownership = models.DateField(default=datetime.now)
    end_date_of_ownership = models.DateField(default=datetime.now)

    def __str__(self):
        return str(str(self.owner) + " " + str(self.vehicle) + " from " + str(self.start_date_of_ownership) + " till " + str(self.end_date_of_ownership))


    def __str__(self):
        return str(self.manufacturer + " " + self.model + " " + self.vehicle_number)

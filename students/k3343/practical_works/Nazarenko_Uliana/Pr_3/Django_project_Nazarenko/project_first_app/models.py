from django.db import models

class Car(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

class CarOwner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
    passport = models.CharField(max_length=200, blank=True, null=True, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

class DriversLicense(models.Model):
    TYPES = (
        ('A', 'type_A'),
        ('B', 'type_B'),
        ('C', 'type_C'),
        ('D', 'type_D'),
        ('M', 'type_M'),

    )
    number = models.CharField(max_length=50)
    date_given = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Info(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.title

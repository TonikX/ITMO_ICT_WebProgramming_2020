from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    state_number = models.CharField(max_length=30)

class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    cars = models.ManyToManyField(Car, through='Owning')

class Owning(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date_owning = models.DateField()
    end_date_owning = models.DateField()

class DrivingLicense(models.Model):
    number_license = models.IntegerField()
    date_giving = models.DateField()
    license_type = (
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
        ('Type 3', 'Type 3')
    )

    type = models.CharField(max_length=6, choices=license_type)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

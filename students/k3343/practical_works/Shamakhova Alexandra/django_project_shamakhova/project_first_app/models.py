from django.db import models


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()


class Car(models.Model):
    car_maker = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_colour = models.CharField(max_length=30)
    car_number = models.CharField(max_length=6)


class Ownership(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_date = models.DateField()
    last_date = models.DateField()


class DriverLicense(models.Model):
    LIC_TYPES = (
        ('A', 'motorcycle'),
        ('B', 'automobile'),
        ('C', 'truck'),
        ('D', 'bus')
    )
    lic_number = models.PositiveIntegerField()
    lic_issue_date = models.DateField()
    lic_type = models.CharField(max_length=1, choices=LIC_TYPES)
    lic_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

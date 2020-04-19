from django.db import models

# Create your models here.


class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class DrivingLicense(models.Model):
    DLType = (
        ('AA1M', 'aa1m'),
        ('BB1M', 'bb1m'),
        ('BB1CC1M', 'bb1cc1m'))
    license_num = models.CharField(max_length=10)
    issue_date = models.DateField()
    type = models.CharField(choices=DLType, max_length=7)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class Car(models.Model):
    producer = models.CharField(max_length=40)
    model = models.CharField(max_length=25)
    color = models.CharField(max_length=40)
    state_num = models.CharField(max_length=17)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    own_starting_date = models.DateField()
    own_expiring_date = models.DateField()

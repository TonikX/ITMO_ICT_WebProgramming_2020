from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    state_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.car_brand}'

class CarOwner(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    passport = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    car = models.ManyToManyField(Car, through='TemporaryOwner')

    def __str__(self):
        return f'User {self.name}'


class DriverLicense(models.Model):
    TYPE_CHOICES = (('A', 'Bike'),
                    ('B', 'Light Rigid'),
                    ('C', 'Medium Rigid'),
                    ('D', 'Heavy Rigid'),
                    ('E', 'Heavy Combination'))

    license_id = models.PositiveIntegerField()
    date_of_issue = models.DateField(blank=True, null=True)
    choice_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    owner = owner_lic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.license_id}'


class TemporaryOwner(models.Model):
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    car_owner = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Car')
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_owner} owned by user with license id {self.driver_license}'

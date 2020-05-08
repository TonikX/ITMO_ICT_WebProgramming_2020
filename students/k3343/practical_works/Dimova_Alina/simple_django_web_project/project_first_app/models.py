from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class Auto(models.Model):
    car_number = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)


class Owner(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default='1900-01-01')
    passport = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    car = models.ManyToManyField(Auto, through='Ownership')

    # renames the instances of the model
    # with their title name

    def __str__(self):
        return self.username


class Ownership(models.Model):
    start_date = models.DateField()
    exp_date = models.DateField()
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Auto, on_delete=models.CASCADE)


class Licence(models.Model):
    TYPE_L = (
        ('A', 'A type'),
        ('B', 'B type'),
        ('C', 'C type'),
        ('D', 'D type')
    )
    owner_lic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(blank=True, choices=TYPE_L, max_length=2)

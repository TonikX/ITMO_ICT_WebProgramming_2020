from django.db import models
from datetime import datetime
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver





# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)


# class Book(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


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
    bdate = models.DateField(default=django.utils.timezone.now)

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


class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    passport = models.TextField(max_length=50, blank=True)
    home_address = models.TextField(max_length=500, blank=True)
    nationality = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return "name: " +str(self.person) + " passport: " + str(self.passport) + " home_address: " + str(self.home_address) + " nationality: " + str(self.nationality)



@receiver(post_save, sender=Person)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(person=instance)

@receiver(post_save, sender=Person)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

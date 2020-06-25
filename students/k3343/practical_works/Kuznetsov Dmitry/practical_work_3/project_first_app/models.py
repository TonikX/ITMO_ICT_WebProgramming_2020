from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.










class Car(models.Model):


    name = models.CharField(max_length=30)


    type = models.CharField(max_length=50)


    colour = models.CharField(max_length=20)


    number = models.IntegerField(null=True)


class Owner(AbstractUser):


    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    date_birth = models.DateField()

    passport = models.IntegerField(null=True)

    address = models.CharField(max_length=50)

    nationality = models.CharField(max_length=50)

    car = models.ManyToManyField(Car, through='Owning')

    def __str__(self):
        car_owner = "%s %s" % (self.first_name, self.last_name)
        return car_owner



class Owning(models.Model):


    own_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)


    start_date = models.DateField()


    end_date = models.DateField()



class Passport(models.Model):


    TYPE_EX = (


        ('1', 'First'),


        ('2', 'Second'),


        ('3', 'Third'),


    )


    own_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    number = models.IntegerField(null=True)


    start_date = models.DateField()


    type = models.CharField(max_length=10, choices=TYPE_EX)
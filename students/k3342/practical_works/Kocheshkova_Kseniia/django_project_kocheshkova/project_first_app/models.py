from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()


class Car(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    colour = models.CharField(max_length=40)
    state_number = models.CharField(max_length=40)


class Ownership(models.Model):
    own_name = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_number = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date_of_ownership = models.DateField()
    finish_date_of_ownership = models.DateField()


class License(models.Model):
    TYPE_CHOICES = (
        ('A', 'Motorcycle'),
        ('B', 'Van'),
        ('C', 'Car'),
        ('D', 'Bus'),
        ('M', 'Motorcar'),
    )
    own_name = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField
    start_date_of_issue = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

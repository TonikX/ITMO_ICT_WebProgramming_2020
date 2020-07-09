from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()

class Car(models.Model):
    mark = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    gov_number = models.CharField(max_length=128)

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Driver_license(models.Model):
    license_number = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    TYPE_LICENSE =(
        ('A', 'MOTO'),
        ('B', 'CAR'),
        ('C', 'TRUNK'),
        ('D', 'BUS'),
        ('M', 'MOPED'),
    )
    type = models.CharField(max_length=2, choices=TYPE_LICENSE)

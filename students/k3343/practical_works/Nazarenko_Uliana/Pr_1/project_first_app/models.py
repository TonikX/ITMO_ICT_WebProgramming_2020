from django.db import models


class Car_owner(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birthday = models.DateField()


class Car(models.Model):
    mark = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    gov_num = models.CharField(max_length=128)
    auto_owner = models.ManyToManyField(Car_owner, through='Ownership')


class Ownership(models.Model):
    person = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class Drivers_lic(models.Model):
    number = models.CharField(max_length=128)
    date_of_issue = models.DateField()
    lic_type = (
        ('Motorbike', 'A'),
        ('Auto', 'B'),
        ('Truck', 'C'),
        ('Bus', 'D'),
        ('Moped', 'M'),
    )
    type = models.CharField(max_length=128, choices=lic_type)
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)

from django.db import models
from django.db.models import ForeignKey


class Auto(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    Number = models.CharField(max_length=10)


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField()
    autos = models.ManyToManyField(Auto, through='Possession')


class Possession(models.Model):
    Date_one = models.DateField()
    Date_two = models.DateField()
    Owner = models.ForeignKey(Owner, related_name='Owner_v', on_delete=models.CASCADE, null=True)
    Auto = models.ForeignKey(Auto, related_name='Auto_o', on_delete=models.CASCADE, null=True)


class Drivel(models.Model):
    Owner = models.ForeignKey(Owner, related_name='Owner_d', on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    date = models.DateField()
    TYPES = (
        ('T1', 'Cтарого образца'),
        ('T2', 'Нового образца'),
        ('T3', 'Самого новго образца'),
    )
    comment_type = models.CharField(max_length=2, choices=TYPES, null=True)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):

    name = models.CharField(max_length=50)

    country = models.CharField(max_length=50)

    contacts = models.CharField(max_length=50)


    def __str__(self):


        return self.name


class Flight(models.Model):

    number = models.CharField(max_length=50)

    flight_company = models.ForeignKey(Company,on_delete=models.CASCADE)

    departure = models.DateTimeField(auto_now=False, auto_now_add=False)

    arrival = models.DateTimeField(auto_now=False, auto_now_add=False)

    type_ex = (


        ('dep', 'отправление'),


        ('arr', 'прибытие'),


    )


    type = models.CharField(max_length=50, choices=type_ex)

    gate_num = models.CharField(max_length=10)


    def __str__(self):


        return self.number



class Comment(models.Model):

    kind_x = (

        ('Выход на посадку', 'Изменение выхода на посадку'),

        ('Что-то не то с рейсом', 'Проблемы с рейсом'),

        ('Потеряшка', 'Потерявшийся пассажир'),


    )


    text = models.CharField(max_length=500)

    date = models.DateTimeField(auto_now_add=False)

    kind = models.CharField(max_length=25, choices=kind_x)

    flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE)

    person = models.ForeignKey(User, on_delete=models.CASCADE)
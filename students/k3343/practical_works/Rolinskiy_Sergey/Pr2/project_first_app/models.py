from django.db import models

# Create your models here.

class Car(models.Model):
    brand=models.TextField(max_length=20)
    model=models.TextField(max_length=40)
    color=models.TextField(max_length=20)
    code=models.TextField(max_length=9)

    def __str__(self):
        return self.model

class Owner(models.Model):
    name=models.TextField(max_length=20)
    surname=models.TextField(max_length=20)
    birthdate=models.DateField()
    cars=models.ManyToManyField(Car,through='Ownership')

    def __str__(self):
        return self.name

class Ownership(models.Model):
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    date_start=models.DateField()
    date_end=models.DateField()

class Certificate(models.Model):
    types=(("A","A"),("B","B"),("C","C"),("D","D"),("E","E"))
    cert_number=models.TextField()
    date_of_getting=models.DateField()
    type=models.CharField(max_length=1,choices=types)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return self.cert_number


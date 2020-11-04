from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.surname


class License(models.Model):
    TYPE_LICENSE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    lic_num = models.CharField(max_length=8)
    start_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_LICENSE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.lic_num

    def __str__(self):
        return self.type


class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=8)
    own = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.mark

    def __str__(self):
        return self.model

    def __str__(self):
        return self.color

    def __str__(self):
        return self.number


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

from django.db import models

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name


class License(models.Model):
    TYPE_LICENSE = (
        ('A1', 'A'),
        ('B1', 'B'),
        ('C1', 'C'),
        ('D1', 'D'),
        ('E1', 'E'),
        ('T1', 'Tm'),
        ('T2', 'Tb'),
    )
    license_number = models.CharField(max_length=6)
    begin_date = models.DateField()
    type = models.CharField(max_length=3, choices=TYPE_LICENSE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_number

    def __str__(self):
        return self.type


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    own = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.brand

    def __str__(self):
        return self.model

    def __str__(self):
        return self.color

    def __str__(self):
        return self.number


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()





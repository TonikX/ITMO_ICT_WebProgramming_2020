from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gov_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    car = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return self.name


class DrivingLicense(models.Model):
    owner_dl = models.ForeignKey(Owner,on_delete=models.CASCADE)
    license_number = models.IntegerField()
    receiving_date = models.DateField()
    TYPE_DL =  [
        ('A', 'license_A'),
        ('B', 'license_B'),
        ('C', 'license_C'),
        ('D', 'license_D'),
        ('E', 'license_E')
    ]
    type = models.CharField(max_length=2, choices=TYPE_DL)

    def __str__(self):
        return self.owner_dl


class Ownership(models.Model):
    owner_car = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.owner_car





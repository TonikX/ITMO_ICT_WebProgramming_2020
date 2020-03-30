from django.db import models


# Create your models here.
class Owner(models.Model):

    class Meta:
        db_table = 'Owner'

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.surname


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    car_number = models.CharField(max_length=30)
    owners = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.colour + ' ' + self.brand + ' ' + self.model


class Ownership(models.Model):

    class Meta:
        db_table = 'Ownership'

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start_own = models.DateField()
    date_end_own = models.DateField()

    def __str__(self):
        return self.owner.name + ' ' + self.owner.surname + ': ' + self.car.brand + ' ' + self.car.model


class DriversLicense(models.Model):

    class Meta:
        db_table = 'DriversLicense'

    DL_TYPES = (
        ('A', 'Motorcycles'),
        ('A1', 'Light motorcycles'),
        ('B', 'Passenger cars, small trucks (up to 3.5 tons)'),
        ('BE', 'Passenger cars with a trailer'),
        ('B1', 'Tricycles'),
        ('C', 'Commercial vehicles (from 3.5 tonnes)'),
        ('CE', 'Trucks with a trailer'),
        ('C1', 'Medium trucks (from 3.5 to 7.5 tons)'),
        ('C1E', 'Medium trucks with trailer'),
        ('D', 'Buses'),
        ('DE', 'Buses with a trailer'),
        ('D1', 'Small buses'),
        ('D1E', 'Small buses with a trailer'),
        ('M', 'Mopeds'),
        ('Tm', 'Trams'),
        ('Tb', 'Trolleybuses')
    )
    license_number = models.CharField(max_length=30)
    date_issue = models.DateField()
    category = models.CharField(max_length=3, choices=DL_TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.name + ' ' + self.owner.surname

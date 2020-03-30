from django.db import models


class Owner(models.Model):

    class Meta:
        db_table = 'Owner'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name


class DriversLicense(models.Model):

    class Meta:
        db_table = 'DriversLicense'

    CLASSES_OF_LICENSES = (('A', 'Class A'),
                           ('B', 'Class B'),
                           ('C', 'Class C'),
                           ('D', 'Class D'),
                           ('M', 'Class M'),
                           ('ACDL', 'Class A CDL'),
                           ('BCDL', 'Class B CDL'),
                           ('CCDL', 'Class C CDL'),
                           ('MCDL', 'Class M CDL'))
    date_of_issue = models.DateField()
    license_number = models.IntegerField()
    category = models.CharField(max_length=4, choices=CLASSES_OF_LICENSES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_number


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    car_number = models.CharField(max_length=7)
    owners = models.ManyToManyField(Owner, through='Ownership') 

    def __str__(self):
        return self.car_number

class Ownership(models.Model):

    class Meta:
        db_table = 'Ownership'

    date_of_start = models.DateField()
    date_of_end = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

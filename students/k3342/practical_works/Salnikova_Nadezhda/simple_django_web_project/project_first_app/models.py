from django.db import models


class Owner(models.Model):

    class Meta:
        db_table = 'Owner'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.last_name


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    car_number = models.CharField(max_length=8)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    owners = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.car_number


class DriverLicense(models.Model):

    class Meta:
        db_table = 'DriverLicense'

    CLASSES_OF_LICENSES = (('A', 'Class A'),
                           ('A1', 'Class A1'),
                           ('B', 'Class B'),
                           ('B1', 'Class B1'),
                           ('C', 'Class C'),
                           ('C1', 'Class C1'),
                           ('D', 'Class D'),
                           ('D1', 'Class D1'),
                           ('BE', 'Class BE'),
                           ('CE', 'Class CE'),
                           ('C1E', 'Class C1E'),
                           ('DE', 'Class DE'),
                           ('D1E', 'Class D1E'),
                           ('M', 'Class M'),
                           ('Tm', 'Class Tm'),
                           ('Tb', 'Class Tb'))
    license_number = models.IntegerField()
    date_of_issue = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=CLASSES_OF_LICENSES)


class Ownership(models.Model):

    class Meta:
        db_table = 'Ownership'

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_start = models.DateField()
    date_of_end = models.DateField()



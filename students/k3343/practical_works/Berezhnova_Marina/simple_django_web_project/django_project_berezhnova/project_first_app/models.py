from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Auto(models.Model):
    manufacture = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gosnumber = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.manufacture, self.model)


class Ownership(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.driver, self.auto)


class DriverLicense(models.Model):
    LICENSE_TYPES = [
        ('A', 'LIC_A'),
        ('B', 'LIC_B'),
        ('C', 'LIC_C')
    ]

    license_number = models.CharField(max_length=30)
    start_date = models.DateField()
    license_type = models.CharField(choices=LICENSE_TYPES, default='A', max_length=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.driver, self.license_type)

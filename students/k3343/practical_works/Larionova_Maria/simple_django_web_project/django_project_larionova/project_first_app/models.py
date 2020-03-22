from django.db import models

# Create your models here.
class Owner(models.Model):
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
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.owner, self.auto)


class OwnerLicense(models.Model):
    LICENSE_TYPES = [
        ('A', 'license_A'),
        ('B', 'license_B'),
        ('C', 'license_C')
    ]

    license_number = models.CharField(max_length=30)
    start_date = models.DateField()
    license_type = models.CharField(choices=LICENSE_TYPES, default='A', max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.owner, self.license_type)

from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.mark, self.model)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.owner, self.car)


class Drivers_license(models.Model):
    LICENSE_TYPES = [
        ('A', 'Type_A'),
        ('B', 'Type_B'),
        ('C', 'Type_C'),
    ]

    license_number = models.CharField(max_length=30)
    start_date = models.DateField()
    license_type = models.CharField(choices=LICENSE_TYPES, max_length=30)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.owner, self.license_type)

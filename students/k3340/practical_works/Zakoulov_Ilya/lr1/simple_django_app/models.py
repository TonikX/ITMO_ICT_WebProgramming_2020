from django.db import models


class Car(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    state_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CarDriverOwn(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    date_begin_own = models.DateField()
    date_end_own = models.DateField()

    def __str__(self):
        return f"{self.driver} - {self.car}"


class DriverLicense(models.Model):
    LICENSE_A = ('a', 'A')
    LICENSE_B = ('b', 'B')
    LICENSE_C = ('c', 'C')
    LICENSE_TYPES = [
        LICENSE_A,
        LICENSE_B,
        LICENSE_C
    ]
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='licenses')
    license_number = models.CharField(max_length=100)
    date_of_issuing = models.DateField()
    license_type = models.CharField(
        max_length=1,
        choices=LICENSE_TYPES,
        default=LICENSE_A[0]
    )

    def __str__(self):
        return f"{self.owner}, type license: {self.license_type}"

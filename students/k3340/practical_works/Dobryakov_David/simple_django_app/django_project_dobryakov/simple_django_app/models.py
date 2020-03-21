from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Auto(models.Model):
    manufacture = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)

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
        ('A', 'LICENSE_A'),
        ('B', 'LICENSE_B'),
        ('C', 'LICENSE_C')
    ]

    license_number = models.CharField(max_length=30)
    issuing_date = models.DateField()
    license_type = models.CharField(choices=LICENSE_TYPES, default='A', max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.owner, self.license_type)


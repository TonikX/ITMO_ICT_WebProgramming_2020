from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDERS, default='F', max_length=1)

    passport = models.CharField(max_length=30, default="default")
    nationality = models.CharField(max_length=30, default="default")
    address = models.CharField(max_length=30, default="address")

    def __str__(self):
        return "{} {}, {}, {}".format(self.first_name, self.last_name, self.age, self.get_gender_display())


class Auto(models.Model):
    manufacture = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    gov_number = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.manufacture, self.model)


class Ownership(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.owner, self.auto)


class OwnerLicense(models.Model):
    LICENSES = [
        ('A', 'LICENSE_A'),
        ('B', 'LICENSE_B'),
        ('C', 'LICENSE_C')
    ]

    license_number = models.CharField(max_length=50)
    issuing_date = models.DateField()
    license = models.CharField(choices=LICENSES, default='A', max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.owner, self.get_license_display())

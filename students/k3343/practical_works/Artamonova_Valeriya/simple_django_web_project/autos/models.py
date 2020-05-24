from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Automobile(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    id_car = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        auto = "%s %s %s" % (self.car_make, self.car_model, self.id_car)
        return auto


class User(AbstractUser):
    passport_number = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=50, blank=True)
    nation = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    autos = models.ManyToManyField(Automobile, through='Owning')

    def __str__(self):
        auto_owner = "%s %s" % (self.first_name, self.last_name)
        return auto_owner

class DriverLicense(models.Model):
    id_license = models.CharField(max_length=50, primary_key=True)
    date_of_issue = models.DateField()
    CategoryType = models.TextChoices('CategoryType','A A1 B B1 C')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Водительское удостоверение"
        verbose_name_plural = "Водительские удостоверения"

    def __str__(self):
        license = "%s %s" % (self.owner,self.id_license)
        return license



class Owning(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    date_of_start_owning = models.DateField()
    date_of_end_owning = models.DateField()

    class Meta:
        verbose_name = "Владение автомобилем"

    def __str__(self):
        owning = "%s владеет %s" % (self.owner,self.car)
        return owning

# Create your models here.

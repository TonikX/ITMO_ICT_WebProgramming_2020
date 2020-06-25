from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Avto(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50, primary_key=True)


class User(AbstractUser):
    birthday_date = models.DateField(default='1900-01-01')
    passport = models.CharField(max_length=30, default="1234567890")
    address = models.CharField(max_length=30, default="default address")
    nationality = models.CharField(max_length=30, default="default nationality")
    avto = models.ManyToManyField(Avto, through='Ownership')

    def __str__(self):
        auto_owner = "%s %s" % (self.first_name, self.last_name)
        return auto_owner


class License(models.Model):
    owner_license = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=50, primary_key=True)
    date_issue = models.DateField()
    CategoryType = models.TextChoices('CategoryType', 'A A1 B B1 C')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=2)


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avto = models.ForeignKey(Avto, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()

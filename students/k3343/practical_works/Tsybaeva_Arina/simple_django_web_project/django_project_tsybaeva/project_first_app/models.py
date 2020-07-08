from django.db import models

# Create your models here.

class Auto(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gov_number = models.IntegerField()

    def __str__(self):
        return self.mark, self.model, self.colour, self.gov_number

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    autos = models.ManyToManyField(Auto, through='Ocupation')

    def __str__(self):
        return self.birth_date, self.last_name, self.first_name


class Ocupation(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class License(models.Model):
    license_number = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    TYPE_LICENSE =(
        ('A', 'MOTO'),
        ('B', 'CAR'),
        ('C', 'TRUNK'),
        ('D', 'BUS'),
        ('M', 'MOPED'),
    )
    type = models.CharField(max_length=2, choices=TYPE_LICENSE)
from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class Auto(models.Model):
    car_number = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    car_owner = models.ManyToManyField(Owner, through='Ownership')


class Ownership(models.Model):
    start_date = models.DateField()
    exp_date = models.DateField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Auto, on_delete=models.CASCADE)


class Licence(models.Model):
    TYPE_L = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    owner_lic = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(blank=True, choices=TYPE_L, max_length=2)
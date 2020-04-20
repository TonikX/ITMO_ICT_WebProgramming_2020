from django.db import models


class AutoOwner(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    autos = models.ManyToManyField(Automobile, through='Owning')


class Automobile(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    id_car = models.CharField(max_length=50, primary_key=True)


class DriverLicense(models.Model):
    id_license = models.CharField(max_length=50, primary_key=True)
    date_of_issue = models.DateField()
    CategoryType = models.TextChoices('CategoryType','A A1 B B1 C')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=2)
    owner = models.ForeignKey(Auto_owner, on_delete=models.CASCADE)



class Owning(models.Model):
    owner = models.ForeignKey(Auto_owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    date_of_start_owning = models.DateField()
    date_of_end_owning = models.DateField()


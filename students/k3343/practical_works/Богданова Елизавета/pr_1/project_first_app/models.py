from django.db import models

class Car_owner(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    id_car = models.CharField(max_length=50, primary_key=True)


class Driver_license(models.Model):
    id_license = models.CharField(max_length=50, primary_key=True)
    date_of_issue = models.DateField()
    CategoryType = models.TextChoices('CategoryType','A B C')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=1)
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)



class Owning(models.Model):
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_start_owning = models.DateField()
    date_of_end_owning = models.DateField()

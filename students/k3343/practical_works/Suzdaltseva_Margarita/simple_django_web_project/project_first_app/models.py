from django.db import models

class Car(models.Model):
    trademark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')

class DriversLicense(models.Model):
    TYPES = (
        ('A','moto'),
        ('B','autoB'),
        ('C','autoC'),
        ('D', 'autoD'),
        ('E', 'autoE'),
        # и так далее
    )
    number = models.CharField(max_length=50)
    date_given = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class ExampleModel(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.title


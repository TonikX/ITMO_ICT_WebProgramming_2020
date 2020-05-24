from django.db import models

class AutoOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.DateField()

class Auto(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gos_number = models.IntegerField()

class Owner(models.Model):
    owner = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    auto =  models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_auto_perion = models.DateField()
    end_auto_perion = models.DateField()

class DriverLicense(models.Model):
    CHOICES = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    number = models.IntegerField()
    date_of_issue = models.DateField()
    type = models.CharField(max_length=1, choices=CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
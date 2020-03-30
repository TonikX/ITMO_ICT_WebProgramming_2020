from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Owner(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    gos_num = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.make, self.model)

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.owner, self.car)

class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    is_date = models.DateField()
    type = models.CharField(max_length=128)
    license = models.CharField(max_length=128)

    TYPES = [
        ('A', 'Type_A'),
        ('B', 'Type_B'),
        ('C', 'Type_C'),
    ]

    def __str__(self):
        return "{} {}".format(self.owner, self.type)
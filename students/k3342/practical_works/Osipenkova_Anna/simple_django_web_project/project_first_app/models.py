from django.db import models


# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.birth_date)


class Auto(models.Model):
    car_number = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    car_owner = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return "{} {} {} {} {}".format(self.car_number, self.brand_name, self.model_name, self.colour, self.car_owner)


class Ownership(models.Model):
    start_date = models.DateField()
    exp_date = models.DateField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.start_date, self.exp_date, self.owner_id, self.car_id)


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

    def __str__(self):
        return "{} {} {} {}".format(self.owner_lic, self.id_number, self.date, self.type)

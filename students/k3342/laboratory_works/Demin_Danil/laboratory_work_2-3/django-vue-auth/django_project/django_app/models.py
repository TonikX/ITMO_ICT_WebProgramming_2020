from django.db import models

class Building(models.Model):
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

class Worker(models.Model):
    passport = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Cage(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    row = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f'Row {self.row}, number {self.number}, at {self.building}'

class Breed(models.Model):
    name = models.CharField(max_length=100)
    avg_weight = models.IntegerField(default=0)
    diet_name = models.CharField(max_length=100)
    avg_productivity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Chicken(models.Model):
    cage_id = models.ForeignKey(Cage, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    productivity = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

class Report(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    cage_id = models.ForeignKey(Cage, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
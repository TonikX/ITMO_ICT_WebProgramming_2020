from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.country, self.city)


class ClubOwner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    owner = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.email, self.phone, self.owner)


class Mountain(models.Model):
    country = models.CharField(max_length=50)
    height = models.IntegerField()
    name = models.CharField(max_length=200)
    is_climbed = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}, {}".format(self.country, self.height, self.name)


class Climber(models.Model):
    INTEREST = [
        ('1', 'Skiing'),
        ('2', 'Ice hockey'),
        ('3', 'Soccer'),
        ('4', 'Basketball'),
        ('5', 'Hockey'),
        ('6', 'Reading'),
        ('7', 'Writing'),
        ('8', 'Oding'),
        ('9', 'Basejump')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(choices=INTEREST, default='1', max_length=1)

    def __str__(self):
        return "{}, {}".format(self.first_name, self.age)


class Group(models.Model):
    climber = models.ManyToManyField(Climber)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}".format(self.climber, self.name)


class Climbing(models.Model):
    STATUS = [
        ('1', 'Запланировано'),
        ('2', 'В процессе'),
        ('3', 'Завершено')
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    climber = models.ForeignKey(Climber, on_delete=models.CASCADE, blank=True, null=True)
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    climbing_date_start = models.DateField()
    climbing_date_end = models.DateField()
    status = models.CharField(choices=STATUS, default='1', max_length=1)

    def __str__(self):
        return "{}, {}, {}".format(self.climber, self.group, self.mountain)

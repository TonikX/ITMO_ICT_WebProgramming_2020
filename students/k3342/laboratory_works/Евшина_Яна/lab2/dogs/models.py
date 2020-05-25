from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class Club(models.Model):
    club_name = models.CharField(max_length=25)
    town_club = models.CharField(max_length=25)

    def __srt__(self):
        return self.club_name


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.IntegerField
    town = models.CharField(max_length=25)
    passsport = models.CharField(max_length=25)
    expert = models.BooleanField(verbose_name='Expert', default=False)

    def __srt__(self):
        return self.last_name


class Dog(models.Model):
    dog_name = models.CharField(max_length=25)
    breed = models.CharField(max_length=25)
    age = models.IntegerField()
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=gender_choice)
    date_of_medicine = models.DateField()
    inspection = models.BooleanField(
        verbose_name='Medicine inspection done', default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __srt__(self):
        return self.dog_name


class Show(models.Model):
    show_name = models.CharField(max_length=25)
    show_town = models.CharField(max_length=25)
    type_choice = [
        ('1', 'one breed'),
        ('not1', 'a lot of breeds'),
    ]
    type = models.CharField(max_length=4, choices=type_choice)
    start_date = models.DateField()
    end_date = models.DateField()

    def __srt__(self):
        return self.show_name


class Ring(models.Model):
    number = models.CharField(max_length=10)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ex1 = models.CharField(max_length=25)
    ex2 = models.CharField(max_length=25)
    ex3 = models.CharField(max_length=25)

    def __srt__(self):
        return self.number


class Registration(models.Model):
    num = models.CharField(max_length=10)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    fee = models.BooleanField(verbose_name='Fee paid', default=False)

    def __srt__(self):
        return self.num


class Perform(models.Model):
    ring = models.ForeignKey(Ring, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class Grade(models.Model):
    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    perform = models.ForeignKey(Perform, on_delete=models.CASCADE)
    points1 = models.IntegerField()
    points2 = models.IntegerField()
    points3 = models.IntegerField()


from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.conf import settings


class Club(models.Model):
    club_name = models.CharField(max_length=25)
    town_club = models.CharField(max_length=25)

    def __str__(self):
        return self.club_name


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_num = models.IntegerField(null=True)
    town = models.CharField(max_length=25)
    passport = models.CharField(max_length=25)
    expert = models.BooleanField(verbose_name='Expert', default=False)

    def __str__(self):
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                              null=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT,
                             null=True)

    def __str__(self):
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

    def __str__(self):
        return self.show_name


class Ring(models.Model):
    show = models.ForeignKey(Show, on_delete=models.PROTECT, null=True)
    ex1 = models.CharField(max_length=25)
    ex2 = models.CharField(max_length=25)
    ex3 = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.show} - ринг {self.id}'


class Registration(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.PROTECT)
    show = models.ForeignKey(Show, on_delete=models.PROTECT)
    fee = models.BooleanField(verbose_name='Fee paid', default=False)

    def __str__(self):
        fee_str = 'paid' if self.fee else 'not paid'

        return f'{self.show} - {self.dog} - {fee_str}'


class Perform(models.Model):
    ring = models.ForeignKey(Ring, on_delete=models.PROTECT)
    dog = models.ForeignKey(Dog, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ring_id} {self.dog}'


class Grade(models.Model):
    expert = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT, null=True)
    perform = models.ForeignKey(Perform, on_delete=models.PROTECT,
                                null=True)
    points1 = models.IntegerField()
    points2 = models.IntegerField()
    points3 = models.IntegerField()

    def __str__(self):
        return f'{self.perform} Эксперт: {self.expert}'


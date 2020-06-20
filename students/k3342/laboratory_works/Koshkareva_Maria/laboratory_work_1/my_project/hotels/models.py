from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django import forms
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField


myUser = get_user_model()


class Profile(models.Model):
    AGE_LIST = (
        (1, '0-10 y.o.'),
        (2, '10-20 y.o.'),
        (3, '20-30 y.o.'),
        (4, '30-40 y.o.'),
        (5, '40-50 y.o.'),
        (6, '50-60 y.o.'),
        (7, '60-70 y.o.'),
        (8, '70-80 y.o.'),
        (9, '80-90 y.o.'),
        (10, '90-... y.o'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(choices=AGE_LIST, default=3)
    country = CountryField()


@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Hotel(models.Model):
    OFFERS = (
        ('wifi', 'Free Wi-Fi'),
        ('parking', 'Parking space'),
        ('nosmoke', 'Non-smoking rooms'),
        ('ac', 'Air Conditioning'),
        ('pool', 'Swimming pool'),
        ('massage', 'Massage'),
        ('nosound', 'Soundproof rooms'),
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    teaser = models.TextField(max_length=400)
    description = models.TextField()
    capacity = models.IntegerField()  # suites/rooms
    facilities = MultiSelectField(choices=OFFERS, default='wifi')
    #facilities = models.CharField(max_length=10,choices=OFFERS)
    contacts = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    WORD_RATE = (
        (1, '1 - Awful'),(2, '2 - Unsatisfactory'),
        (3, '3 - Bad'),(4, '4 - Quite bad'),
        (5, '5 - Average'),(6, '6 - Alright'),
        (7, '7 - Quite good'),(8, '8 - Good'),
        (9, '9 - Great'),(10, '10 - Perfect'),
    )

    TK_LIST = (
        (1, 'Business Traveler'),
        (2, 'Solo Traveler'),
        (3, 'Couple'),
        (4, 'Family with Young Children'),
        (5, 'Family with Teenagers'),
        (6, 'Group Traveler'),
    )

    user = models.ForeignKey(myUser, blank=True, null=True,  on_delete=models.CASCADE)
    one_hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE
    )
    tourist_kind = models.IntegerField(choices=TK_LIST, default=2)
    text = models.TextField()
    vacation_start = models.DateField(default=datetime.date.today)
    vacation_end = models.DateField(default=datetime.date.today)
    rating = models.IntegerField(choices=WORD_RATE, default=5)

    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return "{}".format(self.one_hotel)

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    passport_number = models.IntegerField()
    phone_number = models.IntegerField()


class Flight(models.Model):
    STARS_CHOICES = (
        ('0', 'None'),
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    )
    FLIGHT_CHOICES = (
        ('to hotel', 'to hotel'),
        ('to home city', 'to home city'),
    )
    name_flight = models.CharField(max_length=3)
    company = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=FLIGHT_CHOICES)
    flight_duration = models.TimeField()
    flight_days = models.CharField(max_length=30)
    hotel_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    number_of_stars = models.CharField(max_length=10, choices=STARS_CHOICES)
    number_of_rooms = models.IntegerField()
    family_room = models.BooleanField()
    plane_model = models.CharField(max_length=40)
    number_of_passengers = models.IntegerField()

    def __str__(self):
        return self.name_flight


class Ticket(models.Model):
    name_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    number_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    category = models.CharField(max_length=40)
    row = models.IntegerField()
    place = models.IntegerField()
    date_of_departure = models.DateTimeField()
    date_of_arrival = models.DateTimeField()
    cost = models.IntegerField()


class Comment(models.Model):
    SCORE_CHOICES = (
        ('One', '1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
        ('Six', '6'),
        ('Seven', '7'),
        ('Eight', '8'),
        ('Nine', '9'),
        ('Ten', '10'),
    )
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)
    name_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    comment = models.CharField("Comment", max_length=2000)
    registration_evaluation = models.CharField(max_length=10, choices=SCORE_CHOICES)
    flight_evaluation = models.CharField(max_length=10, choices=SCORE_CHOICES)
    personnel_assessment = models.CharField(max_length=10, choices=SCORE_CHOICES)
    category = models.CharField(max_length=40)
    departure_date = models.DateField()
    post_date = models.DateTimeField("Posted on", auto_now_add=True)


class Reservation(models.Model):
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)
    name_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    passport_number = models.IntegerField()
    phone_number = models.IntegerField()
    category = models.CharField(max_length=40)
    row = models.IntegerField()
    place = models.IntegerField()
    date_of_departure = models.DateTimeField()


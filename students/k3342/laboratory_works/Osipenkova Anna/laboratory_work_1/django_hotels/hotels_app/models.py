from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotel(models.Model):
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    capacity = models.IntegerField()
    comfort = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.address, self.comfort)


class Owner(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}: {}".format(self.name, self.hotel)


class Room(models.Model):
    ROOMTYPES = [
        ('1', '1 персона'),
        ('2', '2 персоны'),
        ('3', '3 персоны'),
        ('4', '4 персоны')
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(choices=ROOMTYPES, default='1', max_length=1)

    def __str__(self):
        return "{}, {}".format(self.hotel, self.get_room_type_display())


class HotelComment(models.Model):
    HOTELRATING = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    period_start = models.DateField()
    period_end = models.DateField()
    text = models.CharField(max_length=768)
    rating = models.CharField(choices=HOTELRATING, default='1', max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

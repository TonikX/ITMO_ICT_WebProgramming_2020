from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hotel(models.Model):
    name = models.CharField("Name", max_length=50)
    address = models.CharField("Address", max_length=200)
    description = models.CharField("Description", max_length=500)
    capacity = models.CharField("Capacity", max_length=500)
    rooms = models.CharField("Rooms", max_length=500)
    comfort = models.CharField("Comfort", max_length=50)
    owner = models.CharField("Owner", max_length=30)

    class Meta:
        db_table = 'Hotel'

    def __str__(self):
        return self.name

class Comment(models.Model):
    rating = [
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
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField("Comment", max_length=2000)
    rating = models.CharField("Rating", choices=rating, max_length=2)
    start = models.DateField("Arrival")
    end = models.DateField("Departure")
    post = models.DateTimeField("Posted on", auto_now_add=True)

    class Meta:
        db_table = 'Comment'

    def __int__(self):
        return self.id
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hotel(models.Model):
    name = models.CharField("Name", max_length=50)
    address = models.CharField("Address", max_length=50)
    description = models.CharField("Description", max_length=250)
    size = models.CharField("Size", max_length=20)
    rooms = models.CharField("Rooms", max_length=50)
    amenities = models.CharField("Amenities", max_length=50)
    owner = models.CharField("Owner", max_length=30)

    def __str__(self):
        return self.name

class Comment(models.Model):
    RATINGS = [(str(i),i) for i in range(1,11)]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField("Comment", max_length=2000)
    rating = models.CharField("Rating", choices=RATINGS, max_length=2)
    start_date = models.DateField("Arrival")
    end_date = models.DateField("Departure")
    post_date = models.DateTimeField("Posted on", auto_now_add=True)
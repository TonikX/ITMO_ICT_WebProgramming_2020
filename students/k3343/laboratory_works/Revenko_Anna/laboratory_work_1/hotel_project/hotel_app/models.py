from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
	address = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	capacity = models.IntegerField()
	comfort = models.CharField(max_length=50)

	def __str__(self):
		return "{}, {}".format(self.name, self.address)


class Owner(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=500)

	def __str__(self):
		return "{}: {}".format(self.fullname, self.hotel)


class Room(models.Model):
	TYPES_OF_ROOM = [
		('1', '1 место'),
		('2', '2 места'),
		('3', '3 места')
	]

	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	type_of_room = models.CharField(choices=TYPES_OF_ROOM, default='1', max_length=1)

	def __str__(self):
		return "{} {}".format(self.hotel, self.get_type_of_room_display())


class Comment(models.Model):
	HOTEL_RATING = [
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
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	rating = models.CharField(choices=HOTEL_RATING, default='1', max_length=2)
	text = models.CharField(max_length=500)
	start_date = models.DateField()
	end_date = models.DateField()

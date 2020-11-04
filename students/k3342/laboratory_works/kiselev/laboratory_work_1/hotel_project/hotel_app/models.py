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
	name = models.CharField(max_length=50)

	def __str__(self):
		return "{}: {}".format(self.name, self.hotel)


class Flat(models.Model):
	FLAT_TYPES = [
		('1', 'Одноместный'),
		('2', 'Двухместный'),
		('3', 'Трёхместный')
	]

	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	flat_type = models.CharField(choices=FLAT_TYPES, default='1', max_length=1)

	def __str__(self):
		return "{} {}".format(self.hotel, self.get_flat_type_display())


class Comment(models.Model):
	HOTEL_STARS = [
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
	star = models.CharField(choices=HOTEL_STARS, default='1', max_length=2)
	text = models.CharField(max_length=500)
	date_start = models.DateField()
	date_end = models.DateField()

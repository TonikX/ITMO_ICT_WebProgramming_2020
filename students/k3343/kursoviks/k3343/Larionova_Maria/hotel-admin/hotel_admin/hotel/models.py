from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Floor(models.Model):
	number = models.IntegerField()

	def __str__(self):
		return 'Floor #{}'.format(self.number)


class Room(models.Model):
	ROOM_TYPES = [
		('1', '1 person'),
		('2', '2 persons'),
		('3', '3 persons')
	]

	ROOM_STATES = [
		('1', 'Free'),
		('2', 'Not free')
	]

	floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
	room_type = models.CharField(choices=ROOM_TYPES, default='1', max_length=1)
	room_state = models.CharField(choices=ROOM_STATES, default='1', max_length=1)
	price = models.IntegerField()

	def __str__(self):
		return '{}, {}. Room type: {}. Is free now? {}.'.format(self.floor, self.price, self.get_room_type_display(), self.get_room_state_display())


class Client(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	city_from = models.CharField(max_length=50)

	def __str__(self):
		return '{} {} {}'.format(self.surname, self.name, self.middle_name)


class ClientRoom(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return '{}, {}. {}'.format(self.client, self.room, self.date)


class Employee(models.Model):
	POSITIONS = [
		('1', 'Administrator'),
		('2', 'Servant')
	]

	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	passport = models.IntegerField()
	position = models.CharField(choices=POSITIONS, default='2', max_length=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {} {}, {}'.format(self.surname, self.name, self.middle_name, self.get_position_display())


class Cleaning(models.Model):
	floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return '{}, {}, {}'.format(self.floor, self.employee, self.date)


class Challengers(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	passport = models.IntegerField()
	birthdate = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return '{} {} {}'.format(self.surname, self.name, self.middle_name)


class Request(models.Model):
	STATES = [
		('1', 'Not hired'),
		('2', 'Hired')
	]

	administrator = models.ForeignKey(Employee, on_delete=models.CASCADE)
	challenger = models.ForeignKey(Challengers, on_delete=models.CASCADE)
	date = models.DateField()
	state = models.CharField(choices=STATES, default='1', max_length=1)

	def __str__(self):
		return '{}, {} | {} by {}'.format(self.challenger, self.date, self.get_state_display(), self.administrator)

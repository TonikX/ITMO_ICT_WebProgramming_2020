from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Floor(models.Model):
	number = models.IntegerField()

	def __str__(self):
		return 'Этаж №{}'.format(self.number)


class Room(models.Model):
	ROOM_TYPES = [
		('1', '1 человек'),
		('2', '2 человека'),
		('3', '3 человека')
	]

	ROOM_STATES = [
		('1', 'Свободна'),
		('2', 'Занята')
	]

	floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
	room_type = models.CharField(choices=ROOM_TYPES, default='1', max_length=1)
	room_state = models.CharField(choices=ROOM_STATES, default='1', max_length=1)
	price = models.IntegerField()

	def __str__(self):
		return '{}, {}. Тип комнаты: {}. {}.'.format(self.floor, self.price, self.get_room_type_display(), self.get_room_state_display())


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
	arrival_date = models.DateField()
	departure_date = models.DateField()

	def __str__(self):
		return '{}, {}. {} - {}'.format(self.client, self.room, self.arrival_date, self.departure_date)


class Employee(models.Model):
	POSITIONS = [
		('1', 'Администратор'),
		('2', 'Служащий'),
		('3', 'Претендент'),
		('4', 'Уволенный')
	]

	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	passport = models.IntegerField()
	position = models.CharField(choices=POSITIONS, default='2', max_length=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	birthdate = models.DateField()
	work_experience = models.IntegerField()

	def __str__(self):
		return '{} {} {}, {}'.format(self.surname, self.name, self.middle_name, self.get_position_display())


class Cleaning(models.Model):
	floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return '{}, {}, {}'.format(self.floor, self.employee, self.date)

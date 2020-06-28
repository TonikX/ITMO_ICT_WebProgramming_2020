from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=250)
	workers_amount = models.IntegerField()
	sides_amount = models.IntegerField() # количество бортов

	def __str__(self):
		return self.name


class Plane(models.Model):
	PLANES_TYPE = [
		('1', 'Passenger'),
		('2', 'Cargo')
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	plane_model = models.CharField(max_length=250)
	seats_num = models.IntegerField()
	plane_type = models.CharField(choices=PLANES_TYPE, max_length=1, default='1')
	plane_speed = models.IntegerField()
	is_repair = models.BooleanField(default=False) # в ремонте или нет?

	def __str__(self):
		return f'{self.plane_model}, {self.get_plane_type_display()}'


class Flight(models.Model):
	saled_tickets_amount = models.IntegerField()
	distance = models.IntegerField()
	arrival_point = models.CharField(max_length=250)
	departure_point = models.CharField(max_length=250)
	is_transit = models.BooleanField(default=False) # наличие транзитных точек
	price = models.IntegerField()

	def __str__(self):
		return f'{self.arrival_point} - {self.departure_point}'


class TransitLanding(models.Model):
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
	arrival_date = models.DateTimeField()
	departure_date = models.DateTimeField()
	landing_point = models.CharField(max_length=250)

	def __str__(self):
		return f'{self.landing_point}, Arrival: {self.arrival_date}, Departure: {self.departure_date}'


class ArrivalDeparture(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
	plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
	arrival_date = models.DateTimeField()
	departure_date = models.DateTimeField()


class Worker(models.Model):
	POSITIONS = [
		('1', 'Captain'),
		('2', 'Second pilot'),
		('3', 'Navigator'), # штурман
		('4', 'Steward'),
		('5', 'Stewardess')
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	patronymic = models.CharField(max_length=250)
	age = models.IntegerField()
	education = models.CharField(max_length=250)
	work_experience = models.IntegerField()
	position = models.CharField(choices=POSITIONS, max_length=1, default='1')
	is_allow = models.BooleanField(default=True) # допущен ли к полёту

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.patronymic}'


class Challenger(models.Model):
	POSITIONS = [
		('1', 'Captain'),
		('2', 'Second pilot'),
		('3', 'Navigator'), # штурман
		('4', 'Steward'),
		('5', 'Stewardess')
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	patronymic = models.CharField(max_length=250)
	age = models.IntegerField()
	education = models.CharField(max_length=250)
	work_experience = models.IntegerField()
	position = models.CharField(choices=POSITIONS, max_length=1, default='1')
	passport = models.IntegerField()
	is_hired = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.patronymic}'


class Crew(models.Model):
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Ticket(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

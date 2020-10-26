from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Plane(models.Model):
	PLANE_TYPES = [
		('1', 'Cargo'),
		('2', 'Passenger')
	]

	plane_type = models.CharField(choices=PLANE_TYPES, default='1', max_length=1)
	seats_amonut = models.IntegerField()
	speed = models.IntegerField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	model = models.CharField(max_length=50)

	def __str__(self):
		return '{}: {} plane {}'.format(self.company, self.plane_type, self.model)


class PlaneState(models.Model):
	STATES = [
		('1', 'In work'),
		('2', 'Under repair')
	]

	plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
	state = models.CharField(choices=STATES, default='1', max_length=1)

	def __str__(self):
		return '{}, {}'.format(self.plane, self.get_state_display())


class Route(models.Model):
	from_point = models.CharField(max_length=50)
	to_point = models.CharField(max_length=50)
	distance = models.IntegerField()

	def __str__(self):
		return 'From {} to {}. Distance {}'.format(self.from_point, self.to_point, self.distance)


class TransitPoints(models.Model):
	ACTIONS = [
		('1', 'Arrival'),
		('2', 'Departure')
	]

	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	date = models.DateField()
	action = models.CharField(choices=ACTIONS, default='1', max_length=1)
	point = models.CharField(max_length=50)

	def __str__(self):
		return 'Route: {}, transit point: {}, {}, {}'.format(self.route, self.point, self.date, self.get_action_display())


class Flights(models.Model):
	date = models.DateField()
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

	def __str__(self):
		return 'Route: {}, {}, {}'.format(self.route, self.plane, self.date)


class Tickets(models.Model):
	STATES = [
		('1', 'Saled'),
		('2', 'Left')
	]

	flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
	amount = models.IntegerField()
	state = models.CharField(choices=STATES, default='1', max_length=1)
	price = models.IntegerField()

	def __str__(self):
		return '{}: {}, {}'.format(self.get_state_display(), self.amount, self.price)


class Employees(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	age = models.IntegerField()
	experience = models.IntegerField()
	passport = models.IntegerField()
	position = models.CharField(max_length=50)

	def __str__(self):
		return "{} {} {}, {}".format(self.last_name, self.first_name, self.middle_name, self.position)


class FlightTeam(models.Model):
	flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
	epmloyee = models.ForeignKey(Employees, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.epmloyee)


class EmloyeeState(models.Model):
	STATES = [
		('1', 'Allow'),
		('2', 'Deny')
	]

	epmloyee = models.ForeignKey(Employees, on_delete=models.CASCADE)
	state = models.CharField(choices=STATES, default='1', max_length=1)
	purpose = models.CharField(max_length=50)

	def __str__(self):
		return '{}, Allow? {}. Purpose: {}'.format(self.epmloyee, self.get_state_display(), self.purpose)


class Challengers(models.Model):
	STATES = [
		('1', 'Received'),
		('2', 'Rejection')
	]

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	age = models.IntegerField()
	experience = models.IntegerField()
	passport = models.IntegerField()
	position = models.CharField(max_length=50)
	state = models.CharField(choices=STATES, default='2', max_length=1)
	email = models.EmailField()

	def __str__(self):
		return "{}: {} {} {}, {} | {}".format(self.company, self.last_name, self.first_name, self.middle_name, self.position, self.get_state_display())


class UserTickets(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flight = models.ForeignKey(Flights, on_delete=models.CASCADE)

	def __str__(self):
		return "{}, {}".format(self.user, self.flight)

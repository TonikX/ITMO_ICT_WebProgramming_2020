from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):

	class Meta:
		db_table = 'Car'

	car_number = models.CharField(max_length=6)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.description


class Team(models.Model):

	class Meta:
		db_table = 'Team'

	name = models.CharField(max_length=30, primary_key=True)
	country = models.CharField(max_length=30)
	number_of_racers = models.IntegerField()

	def __str__(self):
		return self.name


class Racer(models.Model):

	class Meta:
		db_table = 'Racer'

	CLASSES = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D')
	)

	surname = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	middlename = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	experience = models.CharField(max_length=30)
	racer_class = models.CharField(max_length=1, choices=CLASSES)
	team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)

	def __str__(self):
		#return self.name + ' ' + self.surname + ' ' + self.middlename
		return self.name


class Race(models.Model):

	class Meta:
		db_table = 'Race'

	CATEGORIES = (
		('OW', 'Open-wheel racing'),
		('TC', 'Touring car racing'),
		('SpC', 'Sports car racing'),
		('PC', 'Production-car racing'),
		('OM', 'One-make racing'),
		('TAS', 'Time Attack Series'),
		('StC', 'Stock car racing'),
		('R', 'Rallying'),
		('D', 'Drag racing'),
		('OR', 'Off-road racing'),
		('K', 'Kart racing'),
		('H', 'Historical racing'),
		('Other', 'Other')
	)

	name = models.CharField(max_length=30)
	category = models.CharField(max_length=5, choices=CATEGORIES)
	date = models.DateField()
	winner = models.ForeignKey(Racer, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Comment(models.Model):

	class Meta:
		db_table = 'Comment'

	TYPES = (
		('Collaboration', 'Collaboration'),
		('Races', 'Races'),
		('Other', 'Other')
	)

	comment_type = models.CharField(max_length=20, choices=TYPES)
	text = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)
	racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.user)

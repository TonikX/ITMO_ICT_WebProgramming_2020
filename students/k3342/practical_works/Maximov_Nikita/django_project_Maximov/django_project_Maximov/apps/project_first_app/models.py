from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	color = models.CharField(max_length=20)
	plate = models.CharField(max_length=20)
	owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

	def __str__(self):
		return self.plate

class Owner(AbstractUser):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	birth_date = models.DateField()
	passsport = models.IntegerField(default="1")
	address = models.CharField(max_length=100, null=True)
	nationality = models.CharField(max_length=100, null=True)

	def __str__(self):
		return f'{self.last_name} {self.first_name}'

class License(models.Model):
	LICENSE_TYPE = (
		('A', 'Class A'),
		('B', 'Class B'),
		('C', 'Class C'),
		('D', 'Class D'),
		('M', 'Class M'))
	license_id = models.IntegerField()
	issue_date = models.DateField()
	id_type = models.CharField(max_length=1, choices=LICENSE_TYPE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.license_id

class Ownership(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()

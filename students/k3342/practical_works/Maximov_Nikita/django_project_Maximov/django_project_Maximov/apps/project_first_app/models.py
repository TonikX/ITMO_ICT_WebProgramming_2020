from django.db import models

class Car(models.Model):
	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	color = models.CharField(max_length=20)
	plate = models.CharField(max_length=20)

	def __str__(self):
		return self.plate

class Owner(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	birth_date = models.DateField()

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
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

	def __str__(self):
		return self.license_id

class Ownership(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()

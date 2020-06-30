from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	fullname = models.CharField(max_length=250)
	phone_number = models.IntegerField()
	birthdate = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class PatientCard(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateField()
	diagnosis = models.CharField(max_length=250, default='', blank=True, null=True)
	recomendations = models.CharField(max_length=500, default='', blank=True, null=True)


class Doctor(models.Model):
	GENDERS = [
		('1', 'Male'),
		('2', 'Female'),
		('3', 'Non-binary')
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=250)
	specialization = models.CharField(max_length=250)
	degree = models.CharField(max_length=250)
	gender = models.CharField(choices=GENDERS, default='3', max_length=1)
	birthdate = models.DateField()
	first_work_date = models.DateField()
	contract_data = models.CharField(max_length=500)


class Appointment(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateField()


class Payment(models.Model):
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
	amount = models.IntegerField()
	payment_date = models.DateField()
	is_paid = models.BooleanField(default=False)


class Price(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	price = models.IntegerField()


class Calendar(models.Model):
	DAYTYPES = [
		('1', 'Workday'),
		('2', 'Holiday')
	]

	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	date = models.DateField()
	day_type = models.CharField(choices=DAYTYPES, default='1', max_length=1)


class Cabinet(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	cabinet_mode = models.CharField(max_length=250) # режим работы
	responsible = models.CharField(max_length=250)
	phone_number = models.IntegerField()

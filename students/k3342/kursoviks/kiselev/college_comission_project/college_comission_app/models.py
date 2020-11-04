from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Enrollee(models.Model):
	CLASS_CHOICES = [
		('1', 9),
		('2', 11)
	]
	PRIVELEGE_CHOICES = [
		('1', 'Нет привелегий'),
		('2', 'Сирота'),
		('3', 'Инвалид')
	]

	class_type = models.CharField(choices=CLASS_CHOICES, max_length=1, default="1")
	privelege_type = models.CharField(choices=PRIVELEGE_CHOICES, max_length=1, default="1")
	fullname = models.CharField(max_length=1000)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	exam_common = models.IntegerField()
	exam_profile = models.IntegerField()
	certificate_average = models.FloatField()
	certificate = models.CharField(max_length=20)
	passport = models.CharField(max_length=20)


class Faculty(models.Model):
	name = models.CharField(max_length=1000)


class Secretary(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=1000)


class Department(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	name = models.CharField(max_length=1000)


class Spec(models.Model):
	name = models.CharField(max_length=1000)
	minimal_point = models.IntegerField()


class VacantPlace(models.Model):
	STATE_CHOICES = [
		('1', 'Осталось'),
		('2', 'Подано')
	]

	spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
	amount = models.IntegerField()
	state = models.CharField(choices=STATE_CHOICES, default='1', max_length=1)


class DepartmentSpec(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	spec = models.ForeignKey(Spec, on_delete=models.CASCADE)


class Application(models.Model):
	STATE_CHOICES = [
		('1', 'В процессе'),
		('2', 'Не принято'),
		('3', 'Принято')
	]

	enrollee = models.ForeignKey(Enrollee, on_delete=models.CASCADE)
	secretary = models.ForeignKey(Secretary, on_delete=models.CASCADE)
	spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
	application_date = models.DateField()
	state = models.CharField(choices=STATE_CHOICES, default='1', max_length=1)

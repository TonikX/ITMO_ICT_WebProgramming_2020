from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Document(models.Model):
	certificate_num = models.IntegerField() # аттестат
	passport_num = models.IntegerField() # пасспорт

	def __str__(self):
		return f'Certificate {self.certificate_num} Passport {self.passport_num}'


class Exam(models.Model):
	profile_points = models.IntegerField() # профильные
	common_points = models.IntegerField() # общие

	def __str__(self):
		return f'Proile points {self.profile_points} Common points {self.common_points}'


class Certificate(models.Model):
	avg_mark = models.IntegerField() # средний балл аттестата

	def __str__(self):
		return f'{self.avg_mark}'


class Enrollee(models.Model):
	# Абитуриент
	CLASSES = [
		('1', '9'),
		('2', '11')
	]

	PRIVELEGES = [
		('1', 'No'),
		('2', 'Disabled'), # инвалид
		('3', 'Orphan') # сирота
	]

	school_class = models.CharField(choices=CLASSES, default='1', max_length=1)
	privelege = models.CharField(choices=PRIVELEGES, default='1', max_length=1)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50) # отчество

	documents = models.ForeignKey(Document, on_delete=models.CASCADE)
	exams = models.ForeignKey(Exam, on_delete=models.CASCADE)
	certificate_avg = models.ForeignKey(Certificate, on_delete=models.CASCADE)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.patronymic}'


class Faculty(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Department(models.Model):
	# Кафедра
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Specialization(models.Model):
	name = models.CharField(max_length=100)
	free_positions = models.IntegerField() # количество свободных мест
	applications_num = models.IntegerField() # количество поданных заявлений
	minimal_point = models.IntegerField() # проходной балл

	def __str__(self):
		return self.name


class SpecializationRealise(models.Model):
	# Реализация специальности
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)


class Secretary(models.Model):
	# Секретарь приёмной комиссии
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50) # отчество

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.patronymic}'


class Application(models.Model):
	# Заявление
	STATES = [
		('1', 'Accepted'),
		('2', 'Not accepted'),
		('3', 'In process')
	]

	EDUCATION_FORMS = [
		('1', 'Contract'),
		('2', 'Budget')
	]

	specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
	secretary = models.ForeignKey(Secretary, on_delete=models.CASCADE, default=1, blank=True, null=True)
	enrollee = models.ForeignKey(Enrollee, on_delete=models.CASCADE)
	date = models.DateField()
	state = models.CharField(choices=STATES, default='3', max_length=1)
	education_form = models.CharField(choices=EDUCATION_FORMS, default='1', max_length=1)

	def __str__(self):
		return f'Enrollee {self.enrollee}, Specialization {self.specialization}'
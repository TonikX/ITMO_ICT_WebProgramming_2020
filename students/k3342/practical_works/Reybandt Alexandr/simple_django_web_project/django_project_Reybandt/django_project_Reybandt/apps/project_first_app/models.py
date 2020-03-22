from django.db import models

class CarOwner(models.Model):
	first_name = models.CharField('Имя', max_length=50)
	last_name = models.CharField('Фамилия', max_length=50)
	date_of_birth = models.DateField('Дата рождения')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class DriverLicense(models.Model):
	car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	LICENSE_TYPE = (
		('A', 'Мотоциклы'),
		('B', 'Легковые авто'),
		('C', 'Грузовики'),
		('D', 'Автобусы'),
		('M', 'Мопеды'),
	)
	license_id = models.IntegerField('Номер удостоверения')
	date_of_issue = models.DateField('Дата выдачи')
	license_type = models.CharField(max_length=1, choices=LICENSE_TYPE)

	def __str__(self):
		return self.license_type

class Car(models.Model):
	make = models.CharField('Марка',max_length=50)
	model = models.CharField('Модель',max_length=50)
	color = models.CharField('Цвет',max_length=30)
	state_number = models.CharField('Гос номер', max_length=10)
	owner = models.ManyToManyField(CarOwner, through='Ownership')

	def __str__(self):
		return f'{self.make} {self.model}'

class Ownership(models.Model):
	owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_date = models.DateField('Дата начала владения')
	end_date = models.DateField('Дата конца владения')





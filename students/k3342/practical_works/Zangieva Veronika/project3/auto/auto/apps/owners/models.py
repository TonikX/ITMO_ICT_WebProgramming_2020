from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractUser

class Owner(AbstractUser):
	name = models.CharField('Имя', max_length = 200)
	surname =  models.CharField('Фамилия', max_length = 200)
	birth_date = models.DateTimeField('Дата Рождения', max_length = 200)
	passport_num = models.IntegerField('Номер паспорта')
	address = models.CharField('Домашний адрес', max_length = 200)
	nationality = models.CharField('Национальность', max_length = 200)

	REQUIRED_FIELDS = ['name', 'surname', 'birth_date', 'passport_num']


	def __str__(self):
		return f'{self.name} {self.surname}'

	class Meta:
		verbose_name = 'Владелец'
		verbose_name_plural = 'Владельцы'

class Car(models.Model):
	mark = models.CharField('Название марки', max_length = 200)
	c_type =  models.CharField('Модель машины', max_length = 200)
	color = models.CharField('Цвет машины', max_length = 200)
	gov_num = models.IntegerField('Гос. номер', max_length = 200)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.mark)

	class Meta:
		verbose_name = 'Автомобиль'
		verbose_name_plural = 'Автомобили'

	
class Ownership(models.Model):
	car = models.ForeignKey(Car, on_delete = models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	start_date = models.DateTimeField('Дата начала владения', max_length = 200)
	end_date = models.DateTimeField('Дата конца владения', max_length = 200)

	def __str__(self):
		return str(self.start_date)

	class Meta:
		verbose_name = 'Владение'
		verbose_name_plural = 'Владения'

class License(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	license_num = models.IntegerField('Номер', max_length = 200)
	date_out = models.DateTimeField('Дата выдачи', max_length = 200)
	l_type = models.CharField('Тип лицензии', max_length = 200)

	def __str__(self):
		return str(self.license_num)

	class Meta:
		verbose_name = 'Удостоверение'
		verbose_name_plural = 'Удостоверения'

# Create your models here.

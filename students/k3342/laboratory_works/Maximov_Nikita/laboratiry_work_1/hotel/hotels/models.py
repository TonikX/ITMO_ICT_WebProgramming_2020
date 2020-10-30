from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

ROOM_TYPES_CHOICE = (
              ('single', 'single'),
              ('double', 'double'),
              ('triple', 'triple'),
              ('quad', 'quad'))

FACILITIES_CHOICE = (
              ('restaurant', 'Restaurant'),
              ('parking', 'Car parking'),
              ('pool', 'Swimming pool'),
              ('internet', 'Internet'),
              ('fitness', 'Fitness'))

class Hotels(models.Model):
	"""Отели"""
	name = models.CharField("Название", max_length=100)
	adress = models.CharField("Адрес", max_length=150)
	description = models.TextField("Описание")
	capacity = models.IntegerField("Вместимость (человек)")
	room_types = MultiSelectField(choices=ROOM_TYPES_CHOICE)
	facilities = MultiSelectField(choices=FACILITIES_CHOICE)
	hotel_owner = models.CharField("Имя владельца", max_length=100)
	image = models.ImageField("Изображение",upload_to="hotels_photo/")

	def __str__(self):
		return self.name
		
class Comments(models.Model):
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
	rating = models.DecimalField("Оценка - от 1 до 10", max_digits=2, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
	comment_text = models.TextField("Текст отзыва")
	start_period = models.DateField("Дата заезда", default=date.today)
	end_period = models.DateField("Дата выезда", default=date.today)
	contact_info = models.ForeignKey(User, on_delete=models.CASCADE)
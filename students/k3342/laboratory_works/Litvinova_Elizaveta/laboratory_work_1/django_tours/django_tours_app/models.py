from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return "{}".format(self.name)


class PaymentCondition(models.Model):
	CONDITIONS = [
		('1', '100% предоплата'),
		('2', '50% до, 50% после'),
		('3', '70% до, 30% после'),
		('4', '10% скидка')
	]

	condition = models.CharField(choices=CONDITIONS, default='1', max_length=1)

	def __str__(self):
		return "Условия оплаты: {}".format(self.get_condition_display())


class Tour(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	first_date = models.DateField()
	second_date = models.DateField()

	payment_conditions = models.ForeignKey(PaymentCondition, on_delete=models.CASCADE)
	agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

	def __str__(self):
		return "{}: {}, {} - {}".format(self.agency, self.name, self.first_date, self.second_date)


class Comment(models.Model):
	COMMENT_TYPES = [
		('1', 'Вопрос по туру'),
		('2', 'Вопрос по оплате'),
		('3', 'Отзыв')
	]

	tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

	desc = models.CharField(max_length=1000)
	comment_type = models.CharField(choices=COMMENT_TYPES, default='1', max_length=1)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

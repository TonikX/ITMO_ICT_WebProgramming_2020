from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return "{}".format(self.name)


class PaymentCondition(models.Model):
	CONDITIONS_LIST = [
		('1', '100% before the trip'),
		('2', '50% before the trip, 50% after'),
		('3', '70% before the trip, 30% after'),
		('4', '10% off'),
		('5', '90% before the trip, 10% after'),
		('6', '60% before the trip, 40% after')
	]

	conditions = models.CharField(choices=CONDITIONS_LIST, default='1', max_length=1)

	def __str__(self):
		return "Payment conditions: {}".format(self.get_conditions_display())


class Tour(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	start_date = models.DateField()
	end_date = models.DateField()

	payment_conditions = models.ForeignKey(PaymentCondition, on_delete=models.CASCADE)
	agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

	def __str__(self):
		return "{}: {}, {} - {}".format(self.agency, self.name, self.start_date, self.end_date)


class TourComment(models.Model):
	COMMENT_TYPES = [
		('1', 'Tour content question'),
		('2', 'Payment question'),
		('3', 'Review')
	]

	tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

	comment_text = models.CharField(max_length=1000)
	question_type = models.CharField(choices=COMMENT_TYPES, default='1', max_length=1)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

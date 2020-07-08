from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
	TYPES = [
		('1', 'IP'),
		('2', 'OOO')
	]

	name = models.CharField(max_length=50)
	sphere = models.CharField(max_length=50)
	company_type = models.CharField(choices=TYPES, default='2', max_length=1)

	def __str__(self):
		return '{} "{}"'.format(self.get_company_type_display(), self.name)


class Client(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	patronymic = models.CharField(max_length=50)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	phone = models.CharField(max_length=14)

	def __str__(self):
		return '{} {} {}, {}'.format(self.user.last_name, self.user.first_name, self.patronymic, self.company)


class Product(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	thematic = models.CharField(max_length=50)

	def __str__(self):
		return '{}, {}'.format(self.name, self.company)


class Employee(models.Model):
	POSITIONS = [
		('1', 'Supervisor'),
		('2', 'Executor')
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	patronymic = models.CharField(max_length=50)
	position = models.CharField(choices=POSITIONS, default='2', max_length=1)
	phone = models.CharField(max_length=14)

	def __str__(self):
		return '{} {}, {}'.format(self.user, self.patronymic, self.get_position_display())


class Request(models.Model):
	STATES = [
		('1', 'Complete'),
		('2', 'Not complete')
	]

	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	executor = models.ForeignKey(Employee, on_delete=models.CASCADE)
	target = models.CharField(max_length=250)
	state = models.CharField(choices=STATES, default='2', max_length=1)
	materials = models.CharField(max_length=500)
	date = models.DateField()
	is_paid = models.BooleanField(default=False)

	def __str__(self):
		return '{}, State: {}. Executor: {}'.format(self.product, self.get_state_display(), self.executor)


class Service(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField()

	def __str__(self):
		return '{}, {}'.format(self.name, self.price)


class ServiceForRequest(models.Model):
	request = models.ForeignKey(Request, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Payment(models.Model):
	STATES = [
		('1', 'Paid'),
		('2', 'Not paid')
	]

	request = models.ForeignKey(Request, on_delete=models.CASCADE)
	amount = models.IntegerField()
	target = models.CharField(max_length=50)
	billing_date = models.DateField()
	payment_date = models.DateField()
	state = models.CharField(choices=STATES, default='2', max_length=1)

	def __str__(self):
		return '{}, {}. Billing Date: {}. State: {}'.format(self.request, self.amount, self.billing_date, self.get_state_display())

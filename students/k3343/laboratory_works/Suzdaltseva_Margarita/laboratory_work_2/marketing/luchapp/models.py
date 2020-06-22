from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)
    TYPES = [
        ('1','ИП'),
        ('2','ОАО'),
        ('3','ООО'),
        ('4','ЗАО'),
        ('5','ПТ'),
        ('6','ТНВ'),
        ('7','ГКП')
        # и другие виды ОПФ
    ]
    company_type = models.CharField(max_length=1, choices=TYPES)


class Service(models.Model):
    name = models.CharField(max_length=100)
    TYPES = [
        ('1','реклама в СМИ'),
        ('2','наружная реклама'),
        ('3','реклама на транспорте'),
        ('4','реклама на месте продаж'),
        ('5','сувенирка'),
        ('6','печатная реклама'),
        ('7','директ-реклама'),
        ('8','реклама в интернете'),
        ('9','ивент-реклама'),
        ('10', 'другое')
        # и т.д. и т.п.
    ]
    service_type = models.CharField(max_length=2, choices=TYPES)
    price = models.IntegerField()


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    POSITIONS = [
        ('e','executor'),
        ('h','head')
    ]
    position = models.CharField(max_length=1, choices=POSITIONS, default='e')
    phone = models.CharField(max_length=14)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)


class Request(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="1")
    description = models.CharField(max_length=280)
    materials = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True, null=True)
    STATUSES = [
        ('0','in progress'),
        ('1','completed')
    ]
    status = models.CharField(max_length=1, choices=STATUSES, default='0')


class Payment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    amount = models.IntegerField()
    day_requested = models.DateTimeField(auto_now_add=True, null=True)
    day_paid = models.DateTimeField(null=True, blank=True)
    STATUSES = [
        ('0','unpaid'),
        ('1','paid')
    ]
    status = models.CharField(max_length=1, choices=STATUSES, default='0')


class Product(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    image = models.CharField(blank=True, max_length=280)



from django.db import models
from django.contrib.auth.models import User


class Airport(models.Model):
    code = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    class Meta:
        db_table = 'Airport'

    def __str__(self):
        return self.code


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bonus_card = models.CharField(max_length=10)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.last_name


class Flight(models.Model):
    code = models.CharField(max_length=10)
    dep_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='dep_airport')
    dep_time = models.DateTimeField()
    dep_terminal = models.IntegerField(blank=True)
    arr_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arr_airport')
    arr_time = models.DateTimeField()
    arr_terminal = models.IntegerField(blank=True)
    types_of_flights = (('straight', 'straight'), ('charter', 'charter'), ('transfer', 'transfer'), ('stopover', 'stopover'))
    flight_type = models.CharField(max_length=10, choices=types_of_flights)
    gate = models.CharField(max_length=5)
    passengers = models.ManyToManyField(Client, through='Booking')

    class Meta:
        db_table = 'Flight'

    def __str__(self):
        return self.code


class Booking(models.Model):
    code = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField()
    types_of_tickets = (('standard', 'standard'), ('business', 'business'), ('first', 'first'))
    ticket_type = models.CharField(max_length=10, choices=types_of_tickets)

    class Meta:
        db_table = 'Booking'

    def __str__(self):
        return self.code


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    types_of_comments = (('Delay', 'Departure_delay'), ('Gate', 'Gate_changed'), ('Review', 'Review'), ('Other', 'Other'))
    comment_type = models.CharField(max_length=30, blank=True, choices=types_of_comments)
    text = models.CharField(max_length=5000)
    post_date = models.DateTimeField("Date", auto_now_add=True)

    class Meta:
        db_table = 'Comment'

    def __int__(self):
        return self.id

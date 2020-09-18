from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Team(models.Model):
    """ Team model. """
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    number_of_racers = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Team Name: {self.name}'


class Car(models.Model):
    """ Car model. """
    car_model = models.CharField(max_length=50)
    car_number = models.CharField(max_length=6)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.car_model


class RacerProfile(models.Model):
    """ Racer model. """

    RACER_TYPE = [
        ('Pro', 'Professional'),
        ('Middle', 'Amateur'),
        ('Fresh', 'Freshman')
    ]
    NAME_MAX_LENGTH = 20

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    middle_name = models.CharField(max_length=NAME_MAX_LENGTH)
    racer_type = models.CharField(max_length=50, choices=RACER_TYPE)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Racer Name: {self.name} {self.surname} {self.middle_name}'


class Race(models.Model):
    """ Racer model. """

    RACE_TYPES = [
        ('H', 'Historical racing'),
        ('StC', 'Stock car racing'),
        ('K', 'Kart racing'),
        ('TC', 'Touring car racing'),
        ('SpC', 'Sports car racing'),
        ('R', 'Rallying'),
        ('OR', 'Off-road racing'),
        ('PC', 'Production-car racing'),
        ('OM', 'One-make racing'),
        ('TAS', 'Time Attack Series'),
        ('D', 'Drag racing'),
        ('OW', 'Open-wheel racing'),
        ('Other', 'Other')
    ]

    RESULTS = [
        ('Winner', 'Winner'),
        ('Second', '2nd Place'),
        ('Third', '3rd Place')
    ]
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=5, choices=RACE_TYPES)
    place = models.CharField(max_length=50, choices=RESULTS)
    time = models.DateTimeField(default=timezone.now)
    winner = models.ForeignKey(RacerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    TYPES = [
        ('Collaboration', 'Collaboration'),
        ('Races', 'Races'),
        ('Other', 'Other')
    ]
    comment_type = models.CharField(max_length=20, choices=TYPES)
    text = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    racer = models.ForeignKey(RacerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.racer}'

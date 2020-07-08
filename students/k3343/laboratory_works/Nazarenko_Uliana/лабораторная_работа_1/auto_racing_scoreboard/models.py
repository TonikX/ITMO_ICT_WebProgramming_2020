from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    car_number = models.CharField(max_length=6)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Team(models.Model):

    class Meta:
        db_table = 'Team'

    name = models.CharField(max_length=30, primary_key=True)
    country = models.CharField(max_length=30)
    number_of_racers = models.IntegerField()

    def __str__(self):
        return self.name


class Racer(models.Model):

    class Meta:
        db_table = 'Racer'

    CLASSES = (
        ('Class 1', 'Class 1'),
        ('Class 2', 'Class 2'),
        ('Class 3', 'Class 3'),
        ('Class 4', 'Class 4'),
        ('Class 5', 'Class 5'),
    )

    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    racer_class = models.CharField(max_length=10, choices=CLASSES)
    description = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Race(models.Model):

    class Meta:
        db_table = 'Race'

    CATEGORIES = (
        ('Кольцевая гонка', 'Кольцевая гонка'),
        ('Ралли', 'Ралли'),
        ('Трофи', 'Трофи'),
        ('Гонка на выносливость', 'Гонка на выносливость'),
        ('Автокросс', 'Автокросс'),
        ('Автослалом', 'Автослалом'),
        ('Триал', 'Триал'),
        ('Дрэг-рейсинг', 'Дрэг-рейсинг'),
        ('Спринт', 'Спринт'),
        ('Дрифт', 'Дрифт'),
        ('Картинг', 'Картинг'),
        ('Стритрейсинг', 'Стритрейсинг'),
        ('Иное', 'Иное'),
    )

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=21, choices=CATEGORIES)
    date = models.DateField()
    winner = models.ForeignKey(Racer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):

    class Meta:
        db_table = 'Comment'

    TYPES = (
        ('Сотрудничество', 'Сотрудничество'),
        ('Гонки', 'Гонки'),
        ('Иное', 'Иное'),
    )

    comment_type = models.CharField(max_length=20, choices=TYPES)
    text = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user)
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Team(models.Model):
    name = models.CharField('Название', max_length=100)
    def __str__(self):
        return self.name


class Person(models.Model):
    TYPE = (
        (1, 'Механик'),
        (2, 'Пилот'),
    )

    name = models.CharField('ФИО', max_length=100)
    description = models.CharField('Описание', max_length=100)
    type = models.PositiveSmallIntegerField(choices=TYPE, default=1)
    experience = models.FloatField('Опыт', max_length=100)
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=100)
    volume = models.FloatField('Объем мотора', max_length=100)
    hp = models.FloatField('Лошадиные силы', max_length=100)

    def __str__(self):
        return self.name + ", hp:" + str(self.hp)

class Race(models.Model):

    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=100)
    date = models.DateField('Дата')
    result = models.DurationField('Время заезда')
    vehicle = models.ForeignKey(Vehicle, verbose_name='Автомобиль', on_delete=models.CASCADE)
    driver = models.ForeignKey(Person, verbose_name='Пилот', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, verbose_name='Гонка', on_delete=models.CASCADE)

    def count(self):
        count = len(Comment.objects.filter(result_id=self.id))
        return count
    def __str__(self):
        return self.name

class Comment(models.Model):
    TYPE = (
        (1, 'Вопрос о сотрудничестве'),
        (2, 'Вопрос о гонках'),
        (3, 'Иное')
    )

    type = models.PositiveSmallIntegerField(choices=TYPE, default=3, verbose_name='Тип комментария')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.CharField('Текст', max_length=100)
    result = models.ForeignKey(Result, verbose_name='Результат', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
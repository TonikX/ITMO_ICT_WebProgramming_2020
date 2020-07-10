from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Driver(models.Model):
    DR_TYPE = (
        ('Про', 'Профессионал'),
        ('Мид', 'Любитель'),
        ('Нач', 'Новичок'),
    )
    fio = models.CharField(max_length=100)
    command_name = models.CharField(max_length=30)
    dr_class = models.CharField(max_length=20, choices=DR_TYPE)
    races = models.ManyToManyField('Race', through='Participation', blank=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.fio, self.command_name, self.dr_class)


class Car(models.Model):
    brand_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    year_made = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, {1} - {2}'.format(self.brand_name, self.model_name, self.driver.fio)


class Race(models.Model):
    place = models.CharField(max_length=100)
    date = models.DateField()
    # drivers_num = models.IntegerField()
    # racer = models.ManyToManyField(Driver, through='Participation')

    def __str__(self):
        return '{0}, {1}'.format(self.place, self.date)


class Participation(models.Model):
    RES = (
        ('Победа', 'Победитель'),
        ('Приз', 'Призовое место'),
        ('Финиш', 'Финишировал')
    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    result = models.CharField(max_length=20, choices=RES)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.driver.fio, self.race, self.result)


class Comment(models.Model):
    C_TYPES = (
        ('Сотруд-во', 'О сотрудничестве'),
        ('Гонки', 'О гонках'),
        ('Другое', 'Другое'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    text = models.CharField("Текст комментария", max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=C_TYPES)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.type, self.author)

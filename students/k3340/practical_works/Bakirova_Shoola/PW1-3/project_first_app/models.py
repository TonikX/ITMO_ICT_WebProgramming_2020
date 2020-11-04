from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    mark = models.CharField('Марка', max_length=40)
    model = models.CharField('Модель', max_length=25)
    color = models.CharField('Цвет', max_length=40)
    state_num = models.CharField('Гос. номер', max_length=17)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return "{} {}".format(self.mark, self.model)


class User(AbstractUser):
    birth_date = models.DateField('День рождение', null=True, blank=True)
    passport_data = models.CharField('Паспортные данные', max_length=10, null=True, blank=True)
    home_address = models.TextField('Домашний адрес', null=True, blank=True)
    nationality = models.CharField('Национальность', max_length=40, null=True, blank=True)


class DrivingLicense(models.Model):
    DLType = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'))
    license_num = models.CharField('Номер удостоверения', max_length=10)
    issue_date = models.DateField('Дата выдачи')
    type = models.CharField('Тип', choices=DLType, max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Водительское удостоверение"
        verbose_name_plural = "Водительские удостоверения"

    def __str__(self):
        return self.license_num


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    own_starting_date = models.DateField('Дата начала владения')
    own_expiring_date = models.DateField('Дата окончания владения')

    class Meta:
        verbose_name = "Владение"
        verbose_name_plural = "Владения"

    def __str__(self):
        return "{} {}".format(self.car, self.owner)



from django.db import models
from django.contrib.auth.models import User


class AviaCompany(models.Model):
    name = models.CharField("Название авиакомпании", max_length=50)
    country = models.CharField("Страна, которой принадлежит авиакомпания", max_length=50)
    founded_in = models.DateField("Год основания авиакомпании")

    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField("Номер рейса", max_length=10)
    aviacompany = models.ForeignKey(AviaCompany, on_delete=models.CASCADE)
    departure_from = models.CharField("Место вылета", max_length=100)
    departure_time = models.DateTimeField("Дата и время вылета")
    arrival_to = models.CharField("Место прилета", max_length=100)
    arrival_time = models.DateTimeField("Дата и время прилета")
    gate_number = models.CharField("Номер выхода", max_length=10)

    class Meta:
        verbose_name = "Полет"
        verbose_name_plural = "Полеты"

    def __str__(self):
        return self.flight_number+" "+self.departure_from+"-"+self.arrival_to


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.TextChoices('types', 'Информация_о_задержке Изменение_номера_выхода Иное')
    comment_type = models.CharField("Тип комментария", blank=True, choices=types.choices, max_length=50)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.CharField("Текст комментария", max_length=5000)
    post_date = models.DateTimeField("Дата написания", auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

# Create your models here.

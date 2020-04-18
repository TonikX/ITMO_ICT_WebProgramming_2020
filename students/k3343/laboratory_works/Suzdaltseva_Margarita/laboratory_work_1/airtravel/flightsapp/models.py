from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
import datetime


class Company(models.Model):
    """Класс авиакомпаний"""
    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"

    def __str__(self):
        return self.name


class Direction(models.Model):
    """Класс направлений рейсов"""
    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.name

class Gate(models.Model):
    """Класс гейтов"""
    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Гейт"
        verbose_name_plural = "Гейты"

    def __str__(self):
        return self.name


class Flight(models.Model):
    """Класс авиа перелётов"""
    flightnum = models.CharField("Рейс", max_length=7)
    company = models.ForeignKey(
        Company,
        verbose_name = "Компания",
        on_delete = models.CASCADE)
    departure = models.DateTimeField("Отлёт", default=timezone.now, auto_now=False, auto_now_add=False)
    arrival = models.DateTimeField("Прилёт", default=timezone.now, auto_now=False, auto_now_add=False)
    TYPES = (
        ('D','отлёт'),
        ('A','прилёт'),
    )
    flighttype = models.CharField("Тип", max_length=1, choices=TYPES)
    gate = models.ForeignKey(
        Gate,
        verbose_name = "Гейт",
        on_delete = models.SET_NULL,
        null=True)
    direction = models.ForeignKey(
        Direction,
        verbose_name = "Направление",
        on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Авиа перелёт"
        verbose_name_plural = "Авиа перелёты"

    def __str__(self):
        return self.flightnum


class CommentCategory(models.Model):
    """Класс категорий комментариев"""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

    
class Comments(models.Model):
    """Класс комментариев"""
    user = models.ForeignKey(
        User,
        verbose_name = "Пользователь",
        on_delete = models.CASCADE)
    category = models.ForeignKey(
        CommentCategory,
        verbose_name = "Категория",
        on_delete = models.SET_NULL, null=True)
    flight = models.ForeignKey(
        Flight,
        verbose_name = "Авиа перелёт",
       on_delete = models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)


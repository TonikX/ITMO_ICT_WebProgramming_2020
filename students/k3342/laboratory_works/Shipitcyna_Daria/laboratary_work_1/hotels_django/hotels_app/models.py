from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Facilities(models.Model):
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"


class Room_types(models.Model):
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Тип комнаты"
        verbose_name_plural = "Типы комнат"


class Hotel(models.Model):
    name = models.CharField("Название отеля", max_length= 50)
    description = models.TextField("Описание")
    address = models.CharField("Адрес", max_length= 50)
    capacity = models.IntegerField("Вместимость")
    owner = models.CharField("Владелец", max_length=50)
    facilities = models.ManyToManyField(Facilities)
    room_types = models.ManyToManyField(Room_types)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    hotel = models.ForeignKey(
        Hotel,
        verbose_name="Отель",
        on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    start_living = models.DateField("Дата начала проживания")
    end_living = models.DateField("Дата окончания проживания")
    RATINGS = (
        ('1', 'УЖАСНО'),
        ('2', 'ОЧЕНЬ ПЛОХО'),
        ('3', 'ПЛОХО'),
        ('4', 'УДОВЛИТВОРИТЕЛЬНО'),
        ('5', 'СРЕДНЕ'),
        ('6', 'ВЫШЕ СРЕДНЕГО'),
        ('7', 'ХОРОШО'),
        ('8', 'ОЧЕНЬ ХОРОШО'),
        ('9', 'ОТЛИЧНО'),
        ('10', 'ПРЕВОСХОДНО'),
    )
    rating = models.CharField("Рейтинг", max_length=2, choices=RATINGS)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

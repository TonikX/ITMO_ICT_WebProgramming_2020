from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField("Название отеля", max_length=5000)
    address = models.CharField("Адрес", max_length=5000)
    description = models.CharField("Описание", max_length=5000)
    capacity = models.IntegerField("Вместимость")
    room_types = models.CharField("Типы номеров", max_length=5000)
    facilities = models.CharField("Удобства", max_length=5000)
    owner = models.CharField("Имя владельца", max_length=5000)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.TextChoices('types', '1 2 3 4 5 6 7 8 9 10')
    rating = models.CharField("Рейтинг отеля", blank=True, choices=types.choices, max_length=50)
    check_in = models.DateField("Дата заселения")
    check_out = models.DateField("Дата выселения")
    text = models.CharField("Текст комментария", max_length=5000)
    post_date = models.DateTimeField("Дата написания", auto_now_add=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.rating + " " + self.text

# Create your models here.

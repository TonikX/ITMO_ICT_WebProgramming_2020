from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Hotels(models.Model):
    hotel_name = models.CharField("Название отеля", max_length=100)
    hotel_owner = models.CharField("Владелец отеля", max_length=100)
    hotel_address = models.CharField("Адрес отеля", max_length=500)
    hotel_description = models.TextField("Описание отеля", max_length=1000)
    hotel_capacity = models.IntegerField("Вместимость отеля")
    hotel_class = models.CharField("Класс отеля", max_length=50)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    def __str__(self):
        return self.hotel_name


class Rooms(models.Model):
    ROOM_TYPES = (
        ('1', '1 гость'),
        ('2', '2 гостя'),
        ('3', '3 гостя'),
        ('4', '4 гостя'),
        ('6', '6 гостей')
    )
    room_hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room_type = models.CharField("Тип номера", max_length=1, choices=ROOM_TYPES)
    room_price = models.CharField("Цена номера", max_length=20)

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return self.room_type + " " + self.room_price


class Reservations(models.Model):
    reservation_user = models.ForeignKey(User, verbose_name="Клиент", on_delete=models.CASCADE)
    reservation_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    reservation_start = models.DateField()
    reservation_end = models.DateField()

    class Meta:
        verbose_name = "Резервирование"
        verbose_name_plural = "Резервирования"


class Reviews(models.Model):
    REVIEW_RANKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    REVIEW_PERIODS = (
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring')
    )
    review_user = models.ForeignKey(User, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    review_hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    review_rank = models.CharField("Рейтинг", max_length=2, choices=REVIEW_RANKS)
    review_period = models.CharField("Период проживания", max_length=6, choices=REVIEW_PERIODS)
    review_text = models.TextField("Отзыв", max_length=500)
    review_created = models.DateTimeField("Дата создания", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return "Рейтинг: " + self.review_rank + ". " + self.review_text

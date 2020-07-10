from django.db import models


class Floor(models.Model):
    floor_number = models.IntegerField("Номер этажа")
    number_of_rooms = models.IntegerField("Количество комнат на этаже")

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"


class Servant(models.Model):
    fio = models.CharField("ФИО служащего", max_length=300)

    class Meta:
        verbose_name = "Служащий"
        verbose_name_plural = "Служащие"

    def __str__(self):
        return self.fio


class Cleaning(models.Model):
    servant = models.ForeignKey(Servant, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    week_day = models.TextChoices('week_day', 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье')
    day = models.CharField("День недели", blank=True, choices=week_day.choices, max_length=20)

    class Meta:
        verbose_name = "График уборки"
        verbose_name_plural = "Графики уборки"


class RoomType(models.Model):
    types = models.TextChoices('types', 'Одноместный Двухместный Трехместный')
    room_type = models.CharField("Тип номера", blank=True, choices=types.choices, max_length=20)
    price = models.IntegerField("Цена проживания в сутки в рублях")

    class Meta:
        verbose_name = "Тип номера"
        verbose_name_plural = "Типы номеров"

    def __str__(self):
        return self.room_type


class Room(models.Model):
    room_number = models.CharField("Номер комнаты", max_length=4)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    phone_number = models.CharField("Номер телефона", max_length=6)

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return "Номер "+self.room_number


class Resident(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    fio = models.CharField("ФИО проживающего", max_length=200)
    passport_number = models.CharField("Серия и номер паспорта", max_length=10)
    from_town = models.CharField("Прибыл из города", max_length=50)
    check_in = models.DateField("Дата заселения")
    check_out = models.DateField("Дата выселения")

    class Meta:
        verbose_name = "Проживающий"
        verbose_name_plural = "Проживающие"

    def __str__(self):
        return self.fio
# Create your models here.

# Create your models here.

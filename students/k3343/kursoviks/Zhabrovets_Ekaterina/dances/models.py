from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Location(models.Model): # место проведения мастер-класса
    name = models.CharField("Название", max_length=50)
    address = models.CharField("Адрес", max_length=100)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class Hall(models.Model): # танцевальный зал
    name = models.CharField("Название зала", max_length=50)
    cost = models.IntegerField("Стоимость аренды за час")
    capacity = models.IntegerField("Вместимость")
    school = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return self.name


class DanceStyle(models.Model): # танцевальный стиль
    name = models.CharField("Стиль", max_length=50)
    info = models.TextField("Информация о стиле")

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(max_length=20, blank=True)
    telephone = models.CharField("Телефон", max_length=50)
    full_name = models.CharField("Фамилия-Имя", max_length=50)
    style = models.ForeignKey(DanceStyle, verbose_name="Стиль", on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField("Дата Рождения", blank=True, null=True)
    country = models.CharField("Страна", max_length=50)
    is_teacher = models.BooleanField("Статус учителя", default=False)
    biography = models.TextField("О себе")

    def __str__(self):
        return self.username


class Workshop(models.Model): # мастер-класс
    name = models.CharField("Название", max_length=100, default='Мастер-класс')
    choreographer = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Хореографы")
    place = models.ForeignKey(Hall, verbose_name="Место проведения", on_delete=models.CASCADE)
    date = models.DateField("Дата мастер-класса")
    time = models.TimeField("Время")
    duration = models.FloatField("Продолжительность")
    info = models.TextField("Информация")
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Участники", related_name="added_part")
    price = models.IntegerField("Цена за посещение")

    class Meta:
        verbose_name = "Мастер-класс"
        verbose_name_plural = "Мастер-классы"

    def __str__(self):
        return self.name


class QueryForParticipance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Потенциальный участник', on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, verbose_name="Мастер-класс", on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class QueryForTuition(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Потенциальный педагог', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class Feedback(models.Model):
    RATE = (('Отлично', 'Отлично'), ('Хорошо', 'Хорошо'), ('Плохо', 'Плохо'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, verbose_name="Мастер-класс", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateField("Дата добавления", auto_now_add=True, null=True)
    rating = models.CharField("Рейтинг", max_length=20, choices=RATE, default='Хорошо')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return "{}".format(self.user)
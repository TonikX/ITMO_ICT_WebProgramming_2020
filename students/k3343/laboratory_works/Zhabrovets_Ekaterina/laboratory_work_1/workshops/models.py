from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Location(models.Model):
    name = models.CharField("Название", max_length=50)
    address = models.CharField("Адрес", max_length=100)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class DanceStyle(models.Model):
    name = models.CharField("Стиль", max_length=50)
    info = models.TextField("Информация о стиле")

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    def __str__(self):
        return self.name


class Choreographer(models.Model):
    full_name = models.CharField("Фамилия-Имя", max_length=50)
    style = models.ManyToManyField(DanceStyle, verbose_name="Стиль", through='Master')
    country = models.CharField("Страна", max_length=50)
    birth_date = models.DateField()
    biography = models.TextField("О себе")

    class Meta:
        verbose_name = "Хореограф"
        verbose_name_plural = "Хореографы"

    def __str__(self):
        return self.full_name


class Master(models.Model):
    style = models.ForeignKey(DanceStyle, on_delete=models.CASCADE)
    choreographer = models.ForeignKey(Choreographer, on_delete=models.CASCADE)
    head = models.CharField("Хореограф + стиль", max_length=100)

    class Meta:
        verbose_name = "Хореограф-Стиль"
        verbose_name_plural = "Хореографы и стили"

    def __str__(self):
        return self.head


class Workshop(models.Model):
    LEVELS = (('Начинающий', 'Начинающий'), ('Продвинутый', 'Продвинутый'),('Любой', 'Любой'))
    name = models.CharField("Название", max_length=100, default='Мастер-класс')
    heading = models.ManyToManyField(Master, verbose_name="Стиль + Педагог")
    place = models.ForeignKey(Location, verbose_name="Место проведения", on_delete=models.CASCADE)
    date = models.DateField("Дата мастер-класса")
    time = models.TimeField("Время")
    duration = models.IntegerField("Продолжительность")
    cost = models.IntegerField("Цена")
    level = models.CharField("Уроовень подготовки", max_length=20, choices=LEVELS)
    info = models.TextField("Информация")

    class Meta:
        verbose_name = "Мастер-класс"
        verbose_name_plural = "Мастер-классы"

    def __str__(self):
        return self.name


class Comments(models.Model):
    TYPES = (('Оплата', 'Оплата'), ('Дресс-код', 'Дресс-код'), ('Уровень подготовки', 'Уровень подготовки'), ('Другое', 'Другое'))
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, verbose_name="Мастер-класс", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField(default=False)
    type = models.CharField("Тема", max_length=20, choices=TYPES, default='Оплата')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)

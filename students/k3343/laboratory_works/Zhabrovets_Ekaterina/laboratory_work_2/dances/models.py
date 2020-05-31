from django.db import models


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


class Choreographer(models.Model): # хореограф
    full_name = models.CharField("Фамилия-Имя", max_length=50)
    style = models.ForeignKey(DanceStyle, verbose_name="Стиль", on_delete=models.CASCADE)
    country = models.CharField("Страна", max_length=50)
    birth_date = models.DateField()
    biography = models.TextField("О себе")

    class Meta:
        verbose_name = "Хореограф"
        verbose_name_plural = "Хореографы"

    def __str__(self):
        return self.full_name


class Participant(models.Model): # участники
    fullname = models.CharField("Фамилия-Имя", max_length=50)
    telephone = models.CharField("Телефон", max_length=50)
    email = models.EmailField("Email-адрес")
    birth_date = models.DateField("Дата Рождения", blank=True)

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.fullname


class Workshop(models.Model): # мастер-класс
    # STATUSES = (('Грядущий', 'Грядущий'), ('Проведен', 'Проведен'), ('Отменен', 'Отменен'))
    name = models.CharField("Название", max_length=100, default='Мастер-класс')
    choreographer = models.ManyToManyField(Choreographer, verbose_name="Хореографы")
    place = models.ForeignKey(Hall, verbose_name="Место проведения", on_delete=models.CASCADE)
    date = models.DateField("Дата мастер-класса")
    time = models.TimeField("Время")
    duration = models.FloatField("Продолжительность")
    info = models.TextField("Информация")
    # status = models.CharField("Статус", max_length=20, choices=STATUSES, default='Грядущий')
    participants = models.ManyToManyField(Participant, verbose_name="Участники", related_name="added_part", )

    class Meta:
        verbose_name = "Мастер-класс"
        verbose_name_plural = "Мастер-классы"

    def __str__(self):
        return self.name

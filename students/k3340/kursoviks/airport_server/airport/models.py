from django.db import models
from django.contrib.auth.models import User


class AirCarrier(models.Model):
    name = models.CharField("Название авиакомпании", max_length=50)
    country = models.CharField("Страна, которой принадлежит авиакомпания", max_length=50)
    founded_in = models.DateField("Год основания авиакомпании")

    class Meta:
        verbose_name = "Авиаперевозчик"
        verbose_name_plural = "Авиаперевозчики"

    def __str__(self):
        return self.name


class TransitLanding(models.Model):
    landing = models.CharField("Место посадки", max_length=100)
    date_time_landing = models.DateTimeField("Дата и время посадки")
    date_time_takeoff = models.DateTimeField("Дата и время вылета")

    class Meta:
        verbose_name = "Транзитная посадка"
        verbose_name_plural = "Транзитные посадки"

    def __str__(self):
        return self.landing


class Route(models.Model):
    number = models.CharField("Номер маршрута", max_length=10)
    distance = models.IntegerField("Расстояние в км")
    departure_from = models.CharField("Место вылета", max_length=100)
    departure_time = models.DateTimeField("Дата и время вылета")
    arrival_to = models.CharField("Место прилета", max_length=100)
    arrival_time = models.DateTimeField("Дата и время прилета")
    transit_landing = models.ForeignKey(TransitLanding, on_delete=models.CASCADE, null=True, related_name='route')

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"

    def __str__(self):
        return self.departure_from+"-"+self.arrival_to


class Plane(models.Model):
    number = models.CharField("Номер самолета", max_length=10)
    type_categories = models.TextChoices('type_categories', 'Ту-204 Superjet-100 Airbus-A310 Boeing-747')
    type = models.CharField("Тип самолета", blank=True, choices=type_categories.choices, max_length=100)
    number_of_seats = models.IntegerField("Количество сидений")
    speed = models.IntegerField("Скорость самолета км/ч")
    air_carrier = models.ForeignKey(AirCarrier, on_delete=models.CASCADE, related_name="planes")
    on_repairing = models.BooleanField("Находится на ремонте")

    class Meta:
        verbose_name = "Самолет"
        verbose_name_plural = "Самолеты"

    def __str__(self):
        return str(self.id)


class CrewCommander(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    date_of_birth = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=100)
    work_experience = models.IntegerField("Опыт работы в годах")
    flight_admission = models.BooleanField("Допуск на рейс")

    class Meta:
        verbose_name = "Командир экипажа"
        verbose_name_plural = "Командиры экипажа"

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.second_name


class SecondPilot(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    date_of_birth = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=100)
    work_experience = models.IntegerField("Опыт работы в годах")
    flight_admission = models.BooleanField("Допуск на рейс")

    class Meta:
        verbose_name = "Второй пилот"
        verbose_name_plural = "Вторые пилоты"

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.second_name


class Navigator(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    date_of_birth = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=100)
    work_experience = models.IntegerField("Опыт работы в годах")
    flight_admission = models.BooleanField("Допуск на рейс")

    class Meta:
        verbose_name = "Штурман"
        verbose_name_plural = "Штурманы"

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.second_name


class Crew(models.Model):
    crew_commander = models.ForeignKey(CrewCommander, on_delete=models.CASCADE)
    second_pilot = models.ForeignKey(SecondPilot, on_delete=models.CASCADE)
    navigator = models.ForeignKey(Navigator, on_delete=models.CASCADE)
    air_carrier = models.ForeignKey(AirCarrier, on_delete=models.CASCADE, related_name="crews")

    class Meta:
        verbose_name = "Экипаж"
        verbose_name_plural = "Экипажи"


class Steward(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    date_of_birth = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=100)
    work_experience = models.IntegerField("Опыт работы в годах")
    flight_admission = models.BooleanField("Допуск на рейс")
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name="stewards", null=True)

    class Meta:
        verbose_name = "Бортпроводник"
        verbose_name_plural = "Бортпроводники"

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.second_name


class Flight(models.Model):
    number = models.CharField("Номер рейса", max_length=10)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField("Количество проданных билетов")

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    def __str__(self):
        return self.number

# Create your models here.

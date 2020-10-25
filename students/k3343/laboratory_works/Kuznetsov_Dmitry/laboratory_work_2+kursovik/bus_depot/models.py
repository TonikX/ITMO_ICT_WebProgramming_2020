from django.db import models
from datetime import date


class BusType(models.Model):
    bus_type = models.CharField("Тип автобуса по габариам", max_length=100)
    capacity = models.IntegerField('Вместимость')

    class Meta:
        verbose_name = 'Тип автобуса'
        verbose_name_plural = 'Типы автобусов'

    def __str__(self):
        return self.bus_type


class Bus(models.Model):
    number = models.CharField('Номер государственной регистрации автобуса', max_length=10)
    bus_type = models.ForeignKey(BusType, on_delete=models.CASCADE, related_name='buses')

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'

    def __str__(self):
        return self.number


class Driver(models.Model):
    fio = models.CharField("ФИО", max_length=300)
    passport_number = models.CharField("Номер паспорта", max_length=20)
    class_types = models.TextChoices('class_types', '1_класс 2_класс 3_класс')
    driver_class = models.CharField("Водительский класс", blank=True, choices=class_types.choices, max_length=20)
    work_exp = models.IntegerField('Стаж работы')
    salary = models.IntegerField('Оклад')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return self.fio


class Route(models.Model):
    starting_point = models.CharField("Начальный пункт движения", max_length=300)
    final_destination = models.CharField("Конечный пункт движения", max_length=300)
    time_start = models.TimeField('Время начала движения')
    time_end = models.TimeField('Время окончания движения')
    interval_of_movement = models.IntegerField('Интервал движения в минутах')
    length_in_min = models.IntegerField('Протяженность в минутах')
    length_in_km = models.IntegerField('Протяженность в километрах')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.starting_point+' '+self.final_destination


class Schedule(models.Model):
    week_day = models.TextChoices('week_day', 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье')
    day = models.CharField("День недели", blank=True, choices=week_day.choices, max_length=20)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, )
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'


class Journal(models.Model):
    date = models.DateField('Дата', default=date.today)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status_type = models.TextChoices('status_type', 'Вышел_на_линию Не_вышел_на_линию')
    status = models.CharField("Статус", blank=True, choices=status_type.choices, max_length=20)
    comment = models.TextField("Комментарий", blank=True)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'

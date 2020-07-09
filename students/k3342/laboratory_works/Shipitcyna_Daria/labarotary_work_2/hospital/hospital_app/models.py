from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt


class Patient(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    birth_date = models.DateField("Дата рождения", blank=False, default='2000-01-01')
    SEX = (
        ('мужской', 'мужской'),
        ('женский', 'женский'),
    )
    sex = models.CharField("Пол", max_length=7, choices=SEX)
    phone = models.CharField("Номер телефона", max_length=11, blank=False, default="не указан")
    email = models.CharField("Адрес электронной почты", max_length=50, blank=False, default="не указана")

    def __str__(self):
        return self.surname + ' ' + self.name


class App_times(models.Model):
    date = models.DateField("Дата приема", blank=False, null=False, default=dt.now)
    time_start = models.TimeField("Начало времени приема", blank=False, null=False, default=dt.now)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time_start)


class Doctor(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    education = models.CharField("Образование", max_length=300)
    CATEGORIES = (
        ('1', 'Врач 1-ой категории'),
        ('2', 'Врач 2-ой категории'),
        ('3', 'Врач 3-ей категории'),
    )
    SEX = (
        ('мужской', 'мужской'),
        ('женский', 'женский'),
    )
    TYPES = (
        ('гинеколог', 'гинеколог'),
        ('окулист', 'окулист'),
        ('терапевт', 'терапевт'),
        ('кардиолог', 'кардиолог'),
    )
    category = models.CharField("Категория врача", max_length=1, choices=CATEGORIES, blank=True, default='1')
    type = models.CharField("Специализация врача", max_length=11, choices=TYPES, blank=True, default='терапевт')
    sex = models.CharField("Пол", max_length=7, choices=SEX)
    work_times = models.ManyToManyField(App_times, through="Schedule", blank=True)
    phone = models.CharField("Номер телефона", max_length=11, blank=False, default="не указан")
    email = models.CharField("Адрес электронной почты", max_length=50, blank=False, default="не указана")

    def get_fullname(self):
        return self.surname + ' ' + self.name

    def __str__(self):
        return self.get_fullname()


class Schedule(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        verbose_name="Врач",
        on_delete=models.CASCADE
    )
    app_time = models.ForeignKey(App_times, on_delete=models.PROTECT)
    def __str__(self):
        return "{doctor} {date} {time}".format(doctor=self.doctor,
                                                date=self.app_time.date,
                                                time=self.app_time.time_start)


class PriceList(models.Model):
    service = models.CharField("Услуга", max_length=100)
    price = models.IntegerField("Стоимость услуги")

    def __str__(self):
        return self.service


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        verbose_name="Пациент",
        on_delete=models.CASCADE
    )
    service = models.ManyToManyField(PriceList, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    record = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    paid = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "{patient} - {doctor} {date} {time}".format(patient=self.patient,
                                                           doctor=self.record.doctor,
                                                           date=self.record.app_time.date,
                                                           time=self.record.app_time.time_start)

from django.db import models
from datetime import date

from django.urls import reverse


class Teachers(models.Model):
    name = models.CharField("Имя", max_length=40)
    surname = models.CharField("Фамилия", max_length=150)
    class_number = models.PositiveSmallIntegerField("Номер кабинета", blank=True, null=True)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    group = models.CharField("Номер группы", max_length=10,)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.group


class Students(models.Model):
    name = models.CharField("Имя", max_length=40)
    surname = models.CharField("Фамилия", max_length=150)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Номер группы", related_name="group_number")

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Subjects(models.Model):
    name = models.CharField("Название предмета", max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пердмет"
        verbose_name_plural = "Предметы"


class Shedule(models.Model):
    time = models.DateTimeField("Время")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name="Учитель")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Номер группы")



    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


class Rating(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    rating = models.PositiveSmallIntegerField("Оценка")


    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журнал"


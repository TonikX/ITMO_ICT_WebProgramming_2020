from django.db import models
from django.contrib.auth.models import User


class User_profile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    group_number = models.CharField("Номер учебной группы", max_length=5)


    def __str__(self):
        surname = self.surname
        name = self.name
        patronymic = self.patronymic
        student = surname + " " + name + " " + patronymic
        return student


class Teacher(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)

    def __str__(self):
        surname = self.surname
        name = self.name
        patronymic = self.patronymic
        teacher = surname + " " + name + " " + patronymic
        return teacher


class Hometask(models.Model):
    dicipline = models.CharField("Дисциплина", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assigment_date = models.DateField("Дата выдачи домашнего задания")
    period = models.DateField("Период выполнения домашнего задания")
    hw_title = models.CharField("Домашнее адание", max_length=100)
    hw_description = models.CharField("Описание домашнего задания", max_length=8000)
    fines = models.CharField("Информация о штрафах", max_length=8000)


    def __str__(self):
        return self.hw_title


class Comment(models.Model):
    hometask = models.ForeignKey(Hometask, on_delete=models.CASCADE, verbose_name="Домашнее задание")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    comment_types = models.TextChoices('comment_types', 'Вопрос_по_домашнему_заданию Вопрос_о_задолженностях Иное')
    type_of_comment = models.CharField("Тип комментария", blank=True, choices=comment_types.choices, max_length=50)
    importance_types = models.TextChoices('importance_types', 'Срочно Не_срочно')
    type_of_importance = models.CharField("Важность комментария", blank=True, choices=importance_types.choices, max_length=100)
    comment = models.CharField("Комментарий", max_length=8000)
    date_of_comment = models.DateTimeField("Дата написания", auto_now_add=True)


    def __int__(self):
        return self.id

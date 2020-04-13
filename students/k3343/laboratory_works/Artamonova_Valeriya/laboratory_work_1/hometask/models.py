from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    isu = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    group = models.CharField("Группа", max_length=5)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        surname = self.surname
        name = self.name
        second_name = self.second_name
        student = surname + " " + name + " " + second_name
        return student


class Teacher(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        surname = self.surname
        name = self.name
        second_name = self.second_name
        teacher = surname + " " + name + " " + second_name
        return teacher


class Hometask(models.Model):
    subject = models.CharField("Дисциплина", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date_given = models.DateField("Дата выдачи задания")
    deadline = models.DateField("Срок выполнения задания")
    task_name = models.CharField("Задание", max_length=100)
    text_of_task = models.CharField("Описание задания", max_length=5000)
    about_fines = models.CharField("О штрафах", max_length=5000)

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"

    def __str__(self):
        return self.task_name


class Comment(models.Model):
    hometask = models.ForeignKey(Hometask, on_delete=models.CASCADE, verbose_name="Домашнее задание")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    commentTypes = models.TextChoices('commentTypes', 'Вопрос_по_заданию Найденная_ошибка Иное')
    type_of_comment = models.CharField("Тип комментария", blank=True, choices=commentTypes.choices, max_length=50)
    importanceTypes = models.TextChoices('importanceTypes', 'Срочно_и_важно Не_срочно_и_важно Не_очень_срочно_и_не_очень_важно Я_написал_этот_комментарий_потому_что_мне_скучно')
    importance_of_comment = models.CharField("Важность комментария", blank=True, choices=importanceTypes.choices, max_length=100)
    text = models.CharField("Текст комментария", max_length=5000)
    post_date = models.DateTimeField("Дата написания", auto_now_add=True)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __int__(self):
        return self.id

# Create your models here.

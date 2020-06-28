from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Teacher(models.Model):
    """Класс учителей
    """
    title = models.CharField("ФИО", max_length=50)

    class Meta:
        verbose_name = "ФИО"
        verbose_name_plural = "ФИО"

    def __str__(self):
        return self.title


class Homework(models.Model):
    """Класс новостей
    """
    teacher = models.ForeignKey(
        Teacher,
        verbose_name="Учитель",
        on_delete=models.SET_NULL,
        null=True)
    subject_title = models.CharField("Название предемета", max_length=100)
    homework_short = models.TextField("Задание кратко", default= "default_title")
    homework_text = models.TextField("Текст задания")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    deadline = models.DateTimeField("Дэдлайн")
    keywords = models.CharField("Штраф за позднюю сдачу", max_length=50)

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задание"

    def __str__(self):
        return self.subject_title


class Comments(models.Model):
    """Класс комментариев к дз
    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    homework = models.ForeignKey(
        Homework,
        verbose_name="Домашнее задание",
        on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    type = models.TextField("Тип комментария", max_length=50)
    importance = models.CharField("Важность комментария", max_length=50)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)

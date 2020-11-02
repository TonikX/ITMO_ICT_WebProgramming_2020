from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ImportanceComments(models.Model):
    """Класс важности комментария
    """
    title = models.CharField("Важность", max_length=50)

    class Meta:
        verbose_name = "Важность комментария"
        verbose_name_plural = "Важность комментариев"

    def __str__(self):
        return self.title


class TypeComments(models.Model):
    """Класс типа комментария
    """
    title = models.CharField("Тип", max_length=50)

    class Meta:
        verbose_name = "Тип комментария"
        verbose_name_plural = "Типы комментариев"

    def __str__(self):
        return self.title


class Homeworks(models.Model):
    """Класс домашних заданий
    """
    title = models.CharField("Предмет", max_length=100)
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    created = models.DateTimeField("Дата выдачи", auto_now_add=True)
    duration = models.DurationField("Период выполнения")
    text = models.TextField("Текст задания")
    fines = models.CharField("Информация о штрафах", max_length=100)

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Ксласс комментариев к новостям
    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    homework = models.ForeignKey(
        Homeworks,
        verbose_name="Домашнее задание",
        on_delete=models.CASCADE)
    importance = models.ForeignKey(
        ImportanceComments,
        verbose_name="Важность комментария",
        on_delete=models.CASCADE)
    type = models.ForeignKey(
        TypeComments,
        verbose_name="Тип комментария",
        on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    country_live = models.CharField("Страна проживания", max_length=50)

    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    def __str__(self):
        surname = self.surname
        name = self.name
        tourist = name + " " + surname
        return tourist

class Agency(models.Model):
    agency = models.CharField("Название турагентства", max_length=50)

    class Meta:
        verbose_name = "Турагентство"
        verbose_name_plural = "Турагентства"

    def __str__(self):
        return self.agency

class Tours(models.Model):
    tour = models.CharField("Название тура", max_length=50)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    country = models.CharField("Страна", max_length=100)
    period_s = models.DateField("Период тура с")
    period_po = models.DateField("Период тура по")
    summa = models.CharField("Стоимость тура", max_length=50)
    text_of_tour = models.CharField("Описание тура", max_length=5000)
    conditions = models.CharField("Условия оплаты", max_length=5000)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    def __str__(self):
        return self.tour

class Comment(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name="Тур")
    tourist = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    commentTypes = models.TextChoices('commentTypes', 'Вопрос_по_содержанию_тура Вопрос_об_условиях_оплаты Отзыв')
    type_of_comment = models.CharField("Тип комментария", blank=True, choices=commentTypes.choices, max_length=50)
    text = models.CharField("Текст комментария", max_length=5000)
    post_date = models.DateTimeField("Дата отправки", auto_now_add=True)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __int__(self):
        return self.id
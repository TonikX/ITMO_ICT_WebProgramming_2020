from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Info(models.Model):
    """Класс информации о перелетах"""
    flight_number = models.CharField("Номер рейса", max_length=25)
    flight_company = models.CharField("Компания", max_length=100)
    departure = models.DateTimeField("Отлет")
    arrival = models.DateTimeField("Прибытие")

    flight_type_choices = (
        ('arrival', 'arrival'),
        ('departure', 'departure')
    )
    flight_type = models.CharField(
        max_length=20,
        choices=flight_type_choices,
        default='arrival',
    )


    gate_number = models.CharField("Номер выхода", max_length=25)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

    def __str__(self):
        return str(self.flight_number) + " " + str(self.flight_company)


class Comment(models.Model):
    category = models.CharField("Категория", max_length=400, default="no category")
    text = models.CharField("Текст комментария", max_length=400)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    # client = models.ForeignKey(Client, verbose_name="Юзер", on_delete=models.CASCADE, default=1)
    client = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return str(self.client)
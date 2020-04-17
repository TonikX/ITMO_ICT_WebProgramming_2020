from django.db import models
from django.contrib.auth.models import User


class Conference(models.Model):
    name = models.CharField("Конференция", max_length=200)
    topics = models.TextChoices('topicTypes', 'Медицна Спорт Кино История Политика')
    type_of_topics = models.CharField("Тема", blank=True, choices=topics.choices, max_length=50)
    place = models.CharField("Место проведения", max_length=200)
    start = models.DateField("Начало конференции")
    finish = models.DateField("Окончание конференции")
    text_of_conference = models.CharField("Описание конференции", max_length=5000)
    text_of_place = models.CharField("Описание места проведения", max_length=5000)
    terms = models.CharField("Условия участия", max_length=5000)

    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"

    def __str__(self):
        return self.name


class Comment(models.Model):
    conference_name = models.ForeignKey(Conference, on_delete=models.CASCADE, verbose_name="Конференция")
    participant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    commentTypes = models.TextChoices('commentTypes', 'Вопрос_о_возможности_участия Вопрос_о_возможности_опубликования Вопрос_о_месте_проведения Иное')
    type_of_comment = models.CharField("Тип комментария", blank=True, choices=commentTypes.choices, max_length=50)
    text = models.CharField("Текст комментария", max_length=5000)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __int__(self):
        return self.id
# Create your models here.

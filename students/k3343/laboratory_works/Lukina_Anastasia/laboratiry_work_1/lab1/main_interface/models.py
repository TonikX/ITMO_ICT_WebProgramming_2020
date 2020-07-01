from django.db import models
from django.contrib.auth.models import User as Auth_User


class Conference(models.Model):
    title = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    conference_description = models.TextField()
    place_description = models.TextField()
    conditions = models.TextField()
    promo = models.ImageField(default="dd")


class Comment(models.Model):
    TYPES = (
        ('T1', 'Вопрос о возможности участия'),
        ('T2', 'Вопрос о возможности опубликования'),
        ('T3', 'Вопрос о месте проведения'),
        ('T4', 'Иное')
    )

    comment = models.TextField()
    comment_type = models.CharField(max_length=2, choices=TYPES)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(Auth_User, on_delete=models.CASCADE)
    date = models.DateField()


class Theme(models.Model):
    theme = models.CharField(max_length=30)


class Conference_themes(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

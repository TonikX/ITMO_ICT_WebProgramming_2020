from django.db import models
from django.contrib.auth.models import User as Auth_User

# Create your models here.
class Report(models.Model):
    report_name = models.CharField(max_length=60)

class Scientist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    country_from = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    position = models.CharField(max_length=30)
    telephone = models.IntegerField()
    company = models.CharField(max_length=30)


class Conference(models.Model):
    conference_name = models.CharField(max_length=30)
    country_location = models.CharField(max_length=30, null=True)
    town_location = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    conference_date = models.DateField(null=True)

    def __str__(self):
        return self.conference_name


class Section(models.Model):
    section_name = models.CharField(max_length=30)
    section_time = models.TimeField()
    conference_name = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='conference')

    def __str__(self):
        return self.section_name, self.section_time


class Speech(models.Model):
    number_of_speech = models.IntegerField()
    time_of_speech = models.TimeField()
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)




class Comment(models.Model):
    conference = models.ForeignKey(Conference, related_name='conf_com', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    TYPES = (
        ('T1', 'Вопрос о возможности участия'),
        ('T2', 'Вопрос о возможности опубликования'),
        ('T3', 'Вопрос о месте проведения'),
        ('T4', 'Иное')
    )
    comment_type = models.CharField(max_length=2, choices=TYPES, null=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.conference)
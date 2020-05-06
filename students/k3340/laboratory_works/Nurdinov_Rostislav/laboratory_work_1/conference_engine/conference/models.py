from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.address)


class Conference(models.Model):
    conference_name = models.CharField(max_length=50)
    date_start = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.conference_name)


class Section(models.Model):
    name = models.CharField(max_length=50)
    date_start = models.TimeField()
    date_end = models.TimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Speaker(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Lecture(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return "{}".format(self.title)


class Speech(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)


class Comment(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.first_name, self.conference)

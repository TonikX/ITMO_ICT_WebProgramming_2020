from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        surname = self.surname
        name = self.name
        teacher = name + " " + surname
        return teacher


class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    task = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=50)
    givingdate = models.DateField()
    deadline = models.DateTimeField()
    fines = models.CharField(max_length=500)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.task


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    group_number = models.CharField(max_length=50)

    def __str__(self):
        surname = self.surname
        name = self.name
        student = name + " " + surname
        return student


class Comment(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    task = models.ForeignKey(Homework, on_delete=models.CASCADE)
    importance = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    TYPE = [
        ('Вопрос', 'Вопрос'),
        ('Замечена ошибка', 'Замечена ошибка'),
        ('Другое', 'Другое')
    ]
    type = models.CharField(max_length=50, choices=TYPE)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return "{}".format(self.user)









from django.db import models

# Create your models here.


class Homework(models.Model):
    discipline = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    issue_date = models.DateField()
    time_for_doing = models.DurationField()
    task_text = models.TextField()
    fine_info = models.TextField()


class Comment(models.Model):
    CType = (
        ('question', 'question'),
        ('error found', 'error found'),
        ('else', 'else'))
    IType = (
        ('highest', 'highest'),
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low'),
    )
    comment_text = models.TextField()
    commenter = models.CharField(max_length=50)
    comment_type = models.CharField(choices=CType, max_length=11)
    comment_importancy = models.CharField(choices=IType, max_length=7)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
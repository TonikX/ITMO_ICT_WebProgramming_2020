from django.db import models


class Quest(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    welcome_text = models.CharField(max_length=1000)
    farewell_text = models.CharField(max_length=1000)
    penalty_1 = models.TimeField()
    penalty_2 = models.TimeField()


class Task(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    tip_1 = models.CharField(max_length=1000, blank=True)
    tip_2 = models.CharField(max_length=1000, blank=True)


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.answer)

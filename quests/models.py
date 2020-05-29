from django.db import models


class Quest(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    welcome_text = models.CharField(max_length=1000)
    farewell_text = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}, {self.place}"


class Task(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='tasks')
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.content[:20]}..."


class Tip(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tips')
    tip = models.CharField(max_length=200)

    def __set__(self):
        return self.tip


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer


class PenaltyTime(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='penalty_times')
    penalty = models.TimeField()

    def __str__(self):
        return self.penalty

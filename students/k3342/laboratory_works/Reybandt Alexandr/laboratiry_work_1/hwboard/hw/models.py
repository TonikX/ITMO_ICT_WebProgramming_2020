from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
User = get_user_model()

TYPE_CHOICES = [
        ('Вопрос по заданию', 'Вопрос по заданию'),
        ('Найденная ошибка', 'Найденная ошибка'),
        ('Другое', 'Другое'),
    ]

class Homework(models.Model):
    subject = models.CharField("Предмет", max_length=150)
    teacher = models.CharField("Преподаватель", max_length=150)
    # slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField("Текст задания", db_index=True)
    date_issue = models.DateField("Дата выдачи")
    duration = models.DurationField("Период выполнения")
    fines = models.CharField("Комментарий", max_length=150, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашнее задание'
        ordering = ['-date_issue']

    def get_absolute_url(self):
        return reverse('hw_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.subject

class Comment(models.Model):
    commentator = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    comment_importance = models.DecimalField("Важность (от 1 до 5)", max_digits=1, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField("Текст комментария", db_index=True)
    comment_type = models.CharField("Тип комментария", max_length=50, choices=TYPE_CHOICES)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    homework = models.ForeignKey(Homework, verbose_name="Домашнее задание", on_delete=models.CASCADE, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return str(self.commentator)





from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Study_Program(models.Model):
    name = models.TextField(max_length=100, verbose_name='название')
    count = models.IntegerField(verbose_name='количество студентов')

    class Meta:
        verbose_name = 'программа обучения'
        verbose_name_plural = 'программы обучения'

class Study_Place(models.Model):
    name = models.TextField(max_length=100, verbose_name='название')
    place = models.TextField(max_length=100, verbose_name='место')

    TYPE = (
        (1, 'Школа'),
        (2, 'Колледж'),
    )

    type = models.PositiveSmallIntegerField(choices=TYPE, default=1)

    class Meta:
        verbose_name = 'место обучения'
        verbose_name_plural = 'места обучения'

class Abiturient(models.Model): #Модель абитуриента
    surname = models.TextField(max_length=100, verbose_name='фамилия')
    name = models.TextField(max_length=100, verbose_name='имя')
    secondname = models.TextField(max_length=100, verbose_name='отчество')

    DOC_TYPE = (
        (1, 'Паспорт'),
        (2, 'Свидетельство о рождении'),
    )

    document_type = models.PositiveSmallIntegerField(choices=DOC_TYPE, default=1, verbose_name='тип документа')
    document_number = models.TextField(max_length=100, verbose_name='номер документа')

    study_place = models.ForeignKey(Study_Place, verbose_name='место учебы', on_delete=models.CASCADE)
    study_date = models.DateField(verbose_name='дата окончания')

    AWARD_TYPE = (
        (1, 'Нет'),
        (2, 'Серебрянная медаль'),
        (3, 'Золотая медаль'),
    )

    award_type = models.PositiveSmallIntegerField(choices=AWARD_TYPE, default=1, verbose_name='награда')

    STUDY_TYPE = (
        (1, 'очная'),
        (2, 'очно-заочная'),
        (3, 'заочная'),
    )

    study_type = models.PositiveSmallIntegerField(choices=STUDY_TYPE, default=1,  verbose_name='формат обучения')

    CONTRACT_TYPE = (
        (1, 'бюджет'),
        (2, 'платный'),
    )

    contract_type = models.PositiveSmallIntegerField(choices=CONTRACT_TYPE, default=1,  verbose_name='тип обучения')

    STUDENT_TYPE = (
        (1, 'нет'),
        (2, 'целевик'),
        (3, 'инвалид'),
        (4, 'сирота'),
    )

    student_type = models.PositiveSmallIntegerField(choices=STUDENT_TYPE, default=1,  verbose_name='тип студента')

    study_program = models.ForeignKey(Study_Program, verbose_name='программа обучения', on_delete=models.CASCADE)

    marks = models.CharField(max_length=200)

    def set_marks(self, x):
        self.marks = json.dumps(x)

    def get_marks(self):
        return json.loads(self.marks)

    accepted = models.BooleanField(verbose_name='зачислен', default=False)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
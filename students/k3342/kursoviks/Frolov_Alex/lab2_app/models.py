from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject = models.CharField("Предмет", max_length=100)
    profile_types = models.TextChoices('profile_types', 'Профильная_дисциплина Базовая_дисциплина')
    profile = models.CharField("Тип предмета", blank=True, choices=profile_types.choices, max_length=100)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teaching_period = models.DateField("Преподает до")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        name = self.name
        surname = self.surname
        second_name = self.second_name
        teacher = surname + " " + name + " " + second_name
        return teacher


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class Room(models.Model):
    number = models.CharField("Номер кабинета", max_length=4)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='room')
    profile_types = models.TextChoices('profile_types', 'Для_профильных_дисциплин Для_базовых_дисциплин')
    profile = models.CharField("Тип кабинета", blank=True, choices=profile_types.choices, max_length=100)

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        room = self.number + " кабинет"
        return room


class Nclass(models.Model):
    number_types = models.TextChoices('number_types', '1 2 3 4 5 6 7 8 9 10 11')
    number = models.CharField("Класс", blank=True, choices=number_types.choices, max_length=2)
    letter_types = models.TextChoices('letter_types', 'А Б В Г')
    letter = models.CharField("Буква", blank=True, choices=letter_types.choices, max_length=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='nclass')

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        nclass = self.number + " " + self.letter
        return nclass


class Children(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    gender_types = models.TextChoices('gender_types', 'Мужской Женский')
    gender = models.CharField("Пол", blank=True, choices=gender_types.choices, max_length=10)
    nclass = models.ForeignKey(Nclass, on_delete=models.CASCADE, related_name="children")

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        children = self.surname + " " + self.name + " " + self.second_name
        return children


class Grade(models.Model):
    student = models.ForeignKey(Children, on_delete=models.CASCADE, related_name="grades")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_types = models.TextChoices('grade_types', '2 3 4 5')
    grade = models.CharField("Оценка за четверть", blank=True, choices=grade_types.choices, max_length=2)

    class Meta:
        unique_together = [
            ("student", "subject", "grade")
        ]
        verbose_name = "Четвертная оценка"
        verbose_name_plural = "Четвертные оценки"

    def __str__(self):
        grade = self.grade
        return grade


class Timetable(models.Model):
    nclass_name = models.ForeignKey(Nclass, on_delete=models.CASCADE, related_name="timetable")
    lesson_number = models.TextChoices('lesson_number',
                                       '1-8:30-9:10 2-9:20-10:00 3-10:10-10:50 4-11:00-11:40 5-12:10-12:50 6-13:10-13:50 7-14:00-14:40 8-14:45-15:25')
    lesson = models.CharField("Урок", blank=True, choices=lesson_number.choices, max_length=50)
    choose_day = models.TextChoices('choose_day', 'Понедельник Вторник Среда Четверг Пятница Суббота')
    day = models.CharField("День недели", blank=True, choices=choose_day.choices, max_length=100)
    subject_name = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, verbose_name="Кабинет", on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ("nclass_name", "lesson", "day")
        ]
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        timetable = self.day + " " + self.lesson
        return timetable
# Create your models here.

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
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teaching_period = models.DateField("Преподает до")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        first_name = self.first_name
        last_name = self.last_name
        second_name = self.second_name
        teacher = last_name + " " + first_name + " " + second_name
        return teacher


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class Cabinet(models.Model):
    number = models.CharField("Номер кабинета", max_length=4)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='cabinet')
    profile_types = models.TextChoices('profile_types', 'Для_профильных_дисциплин Для_базовых_дисциплин')
    profile = models.CharField("Тип кабинета", blank=True, choices=profile_types.choices, max_length=100)

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        cabinet = self.number + " кабинет"
        return cabinet


class Klass(models.Model):
    number_types = models.TextChoices('number_types', '1 2 3 4 5 6 7 8 9 10 11')
    number = models.CharField("Класс", blank=True, choices=number_types.choices, max_length=2)
    litera_types = models.TextChoices('litera_types', 'А Б В Г Д Е')
    litera = models.CharField("Литера", blank=True, choices=litera_types.choices, max_length=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='klass')

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        klass = self.number + " " + self.litera
        return klass


class Pupil(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    gender_types = models.TextChoices('gender_types', 'Мужской Женский')
    gender = models.CharField("Пол", blank=True, choices=gender_types.choices, max_length=10)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name="pupils")

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        pupil = self.last_name + " " + self.first_name + " " + self.second_name
        return pupil


class Grade(models.Model):
    student = models.ForeignKey(Pupil, on_delete=models.CASCADE, related_name="grades")
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
    klass_name = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name="timetable")
    lesson_number = models.TextChoices('lesson_number', '1-8:00-8:45 2-8:50-9:35 3-9:40-10:25 4-10:40-11:25 5-11:30-12:15 6-12:20-13:05 7-13:05-13:50 8-14:00-14:45')
    lesson = models.CharField("Урок", blank=True, choices=lesson_number.choices, max_length=50)
    choose_day = models.TextChoices('choose_day', 'Понедельник Вторник Среда Четверг Пятница Суббота')
    day = models.CharField("День недели", blank=True, choices=choose_day.choices, max_length=100)
    subject_name = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, verbose_name="Учитель",  on_delete=models.CASCADE)
    cabinet_number = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ("klass_name", "lesson", "day")
        ]
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        timetable = self.day + " " + self.lesson
        return timetable

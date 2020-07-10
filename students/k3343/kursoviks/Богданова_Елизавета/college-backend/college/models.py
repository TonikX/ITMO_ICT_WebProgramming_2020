from django.db import models


class Faculty(models.Model):
    name = models.CharField('Название факультета', max_length=100)
    address = models.CharField('Адрес деканата факультета', max_length=100)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField('Название специальности', max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='specialties')
    budget = models.IntegerField('Количество мест на бюджет', null=True)
    contract = models.IntegerField('Количество мест на контракт', null=True)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name


class Enrollee(models.Model):
    fio = models.CharField('ФИО', max_length=200)
    school = models.CharField('Учебное заведение', max_length=100)
    finish_school = models.DateField('Дата окончания учебного заведения')
    medal_type = models.TextChoices('medal_type', 'Золотая Серебряная Отсутствует')
    medal = models.CharField('Медаль', blank=True, choices=medal_type.choices, max_length=100)
    passport_number = models.CharField('Номер паспорта', max_length=10)
    address = models.CharField('Адрес', max_length=200)
    privileges_type = models.TextChoices('privileges_type', 'Инвалид Сирота Нет')
    privileges = models.CharField('Льготы', blank=True, choices=privileges_type.choices, max_length=100)
    target = models.BooleanField('Целевой прием')

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'

    def __str__(self):
        return self.fio


class Application(models.Model):
    enrollee = models.ForeignKey(Enrollee, on_delete=models.CASCADE, related_name='apps')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    date = models.DateField('Дата регистрации заявки')
    status_type = models.TextChoices('status_type', 'Зачислен В_очереди Не_зачислен')
    status = models.CharField('Статус заявки', blank=True, choices=status_type.choices, max_length=100)
    form_type = models.TextChoices('form_type', 'Очная Очно-заочная Заочная')
    form_types = models.CharField('Форма обучения', blank=True, choices=form_type.choices, max_length=100, default='Очная')
    budget_type = models.TextChoices('budget_type', 'Бюджет Контракт')
    form = models.CharField('Поступление на', blank=True, choices=budget_type.choices, max_length=100)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class EGE(models.Model):
    enrollee = models.OneToOneField(Enrollee, on_delete=models.CASCADE, related_name='ege')

    class Meta:
        verbose_name = 'Сертификат ЕГЭ'
        verbose_name_plural = 'Сертификаты ЕГЭ'


class EgeSubject(models.Model):
    ege = models.ForeignKey(EGE, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField('Дисциплина', max_length=50)
    mark = models.IntegerField('Балл')

    class Meta:
        verbose_name = 'Дисциплина ЕГЭ'
        verbose_name_plural = 'Дисциплины ЕГЭ'


class Attestat(models.Model):
    enrollee = models.OneToOneField(Enrollee, on_delete=models.CASCADE, related_name='attestat')
    average = models.FloatField('Средний балл аттестата')

    class Meta:
        verbose_name = 'Аттестат'
        verbose_name_plural = 'Аттестаты'


class AttestatSubject(models.Model):
    attestat = models.ForeignKey(Attestat, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField('Дисциплина', max_length=50)
    mark = models.IntegerField('Балл')

    class Meta:
        verbose_name = 'Дисциплина аттестата'
        verbose_name_plural = 'Дисциплины аттестата'
# Create your models here.

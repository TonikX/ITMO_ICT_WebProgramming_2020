from django.db import models


class Doctor(models.Model):
    "Врачи"
    name = models.TextField("Имя")
    surname = models.TextField("Фамилия")
    middle_name = models.TextField("Отчество")
    specialty = models.TextField("Специальность")
    education = models.TextField("Образование")
    MAN = 'М'
    WOMAN = 'Ж'
    SEX_CHOICES = [
        (MAN, 'Man'),
        (WOMAN, 'Woman'),
    ]
    sex = models.CharField(
        "Пол",
        max_length=1,
        choices=SEX_CHOICES,
        default=MAN,
    )
    bdate = models.DateField()
    start_contract = models.DateField()
    end_contract = models.DateField()

    def __str__(self):
        return str(self.name) + " " + str(self.surname)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"



class Patient(models.Model):
    "Клиенты"
    name = models.TextField("Имя")
    surname = models.TextField("Фамилия")
    phone = models.CharField("Номер телефона", max_length=11)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Medicalrecord(models.Model):
    "Мед. Карты"
    patient = models.OneToOneField(Patient, verbose_name="пациент", on_delete=models.CASCADE)
    diseases = models.TextField("Заболевания")
    date_of_acceptance = models.DateField("Дата принятия")
    diagnosis = models.TextField("Диагноз")
    recommendations_for_treatment = models.TextField("Рекомендации по лечению")

    class Meta:
        verbose_name = "Мед. Карта"
        verbose_name_plural = "Мед. Карты"

    def __str__(self):
        return str(self.patient) + " " + str(self.diseases)


class Scheduleofdoctors(models.Model):
    "Расписание"
    doctor = models.OneToOneField(Doctor, verbose_name="доктор", on_delete=models.CASCADE)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    operating_time = models.TextField("Время работы")

    def __str__(self):
        return str(self.doctor.name) + " " + str(self.doctor.surname)

    class Meta:
        verbose_name = "Раписание"
        verbose_name_plural = "Раписание"


class Cabinet(models.Model):
    "Кабинеты"
    cabinet_number = models.CharField("Номер кабинета", max_length=3)
    operating_time = models.TextField("Время работы")
    telephone = models.CharField("Телефона", max_length=11)
    responsible = models.ForeignKey('Doctor', verbose_name="Ответственный", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.cabinet_number) + " " + str(self.responsible) + " " + str(self.telephone)

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"


class Transactions(models.Model):
    "Оплата"
    doctor = models.ForeignKey('Doctor', verbose_name="Доктор", on_delete=models.CASCADE,)
    patients = models.ForeignKey('Patient', verbose_name="Пациент", on_delete=models.CASCADE,)
    date = models.DateField("Дата")
    price = models.TextField("Цена", max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.doctor.name) + " " + str(self.doctor.surname) + " " + str(self.patients.name) + " " + str(self.patients.surname) + " " + str(self.price) + " Оплачено: " + str(self.paid)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


class Reception(models.Model):
    doctor = models.ForeignKey('Doctor', verbose_name="Доктор", on_delete=models.CASCADE, )
    patients = models.ForeignKey('Patient', verbose_name="Пациент", on_delete=models.CASCADE, )
    date = models.DateField("Дата")
    time = models.TextField("Время", max_length=100)

    def __str__(self):
        return str(self.doctor.surname) + " " + str(self.patients.surname) + " " + str(self.date)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Запись"


class Reviews(models.Model):
    reception = models.ForeignKey('Reception', verbose_name="Запись", on_delete=models.CASCADE, )
    review = models.TextField("Отзыв", max_length=100)


    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return str(self.reception) + " " + str(self.review)
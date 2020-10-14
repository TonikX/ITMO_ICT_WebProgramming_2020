from django.db import models


class Education(models.Model):
    name = models.CharField("Образование", max_length=300)

    class Meta:
        verbose_name = 'Образование'

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField("Название", max_length=300)

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField("Название", max_length=300)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='professions')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.name


class Applicant(models.Model):
    fio = models.CharField("ФИО", max_length=300)
    age = models.IntegerField("Возраст")
    address = models.CharField("Адрес", max_length=300)
    work_experience = models.IntegerField("Опыт работы")
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self):
        return self.fio


class Resume(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='resumes')
    salary = models.IntegerField("Зарплата")
    rank = models.CharField("Разряд", max_length=300)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'


class Course(models.Model):
    name = models.CharField("Название", max_length=300)
    author = models.CharField("Автор курса", max_length=300)
    lasting = models.IntegerField("Продолжительность")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    rank = models.CharField("Разряд", max_length=300)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class CourseCertificate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='courses_certificates')

    class Meta:
        verbose_name = 'Сертификат курса'
        verbose_name_plural = 'Сертификаты курсов'


class Gratuity(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='gratuities')
    salary = models.IntegerField("Размер последней зарплаты")
    date_start = models.DateField("Дата начала выплаты")
    date_end = models.DateField("Дата окончания выплаты")

    class Meta:
        verbose_name = 'Пособие'
        verbose_name_plural = 'Пособия'

    def __int__(self):
        return self.salary*0.7


class Employer(models.Model):
    name = models.CharField("Название", max_length=300)
    contact = models.CharField("Контактное лицо", max_length=300)
    address = models.CharField("Адрес", max_length=300)
    inn = models.CharField("ИНН", max_length=10)
    email = models.EmailField()
    phone = models.CharField("Контактный телефон", max_length=12)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    status_type = models.TextChoices('status_type', 'Открыта Закрыта')
    status = models.CharField("Статус", blank=True, choices=status_type.choices, max_length=20)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    date = models.DateField("Дата регистрации вакансии")
    salary = models.IntegerField("Зарплата")
    types = models.TextChoices('types', 'Стажировка Постоянная Временная Сезонная Дистанционная')
    type = models.CharField("Характер работы", blank=True, choices=types.choices, max_length=20)
    work_experience = models.IntegerField("Опыт работы")
    rank = models.CharField("Разряд", max_length=300)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Application(models.Model):
    status_types = models.TextChoices('status_types', 'Одобрена В_процесе Отклонена')
    status = models.CharField("Статус", blank=True, choices=status_types.choices, max_length=20)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='applications')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    date = models.DateField("Дата подачи")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

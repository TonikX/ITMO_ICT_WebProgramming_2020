from django.db import models


class Book(models.Model):
    name = models.CharField('Название книги', max_length=200)
    author = models.CharField('Автор', max_length=200)
    publisher = models.CharField('Издательство', max_length=100)
    year = models.CharField('Год издания',max_length=4)
    section_type = models.TextChoices('section_type', 'Художественная_литература Учебная_литература Научная_литература Докуентальная_литература')
    section = models.CharField('Секция', blank=True, choices=section_type.choices, max_length=50)
    cipher = models.CharField('Шифр книги', max_length=30)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name


class ReadingRoom(models.Model):
    name = models.CharField('Название читального зала', max_length=50)
    capacity = models.IntegerField('Вместимость')

    class Meta:
        verbose_name = "Читальный зал"
        verbose_name_plural = "Читальные залы"

    def __str__(self):
        return "Читальный зал "+self.name


class BookPlace(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='places')
    reading_room = models.ForeignKey(ReadingRoom, on_delete=models.CASCADE)
    number = models.IntegerField('Количество экземпляров')

    class Meta:
        verbose_name = "Расположение книги"
        verbose_name_plural = "Расположение книги"


class Reader(models.Model):
    library_card = models.CharField('Номер читательского билета', max_length=16)
    fio = models.CharField('ФИО', max_length=200)
    passport_number = models.CharField('Номер паспорта', max_length=12)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=200)
    phone = models.CharField('Номер телефона', max_length=13)
    education_type = models.TextChoices('section_type', 'Начальное Среднее_неоконченное Среднее Высшее_неоконченное Высшее')
    education = models.CharField('Образование', blank=True, choices=education_type.choices, max_length=50)
    academic = models.BooleanField('Наличие ученой степени')
    reading_room = models.ForeignKey(ReadingRoom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return self.fio


class TakingBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='books')
    date_take = models.DateField('Дата взятия книги')
    date_back = models.DateField('Дата возврата книги')

    class Meta:
        verbose_name = "Взятие книги"
        verbose_name_plural = "Взятие книги"
# Create your models here.

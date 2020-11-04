from django.db import models


class Book(models.Model):
    section_type = [
        ('Художественная', 'Художественная литература'),
        ('Учебная', 'Учебная литература'),
        ('Психология', 'Психология'),
        ('Детские', 'Детская литература'),
    ]

    name = models.CharField('Название книги', max_length=200)
    author = models.CharField('Автор', max_length=200)
    publisher = models.CharField('Издательство', max_length=100)
    year = models.CharField('Год издания', max_length=4)
    section = models.CharField('Раздел', choices=section_type, max_length=50)
    cipher = models.CharField('Шифр книги', max_length=30)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name


class Reader(models.Model):
    education_type = (
        ('Дошкольное', 'Дошкольное'),
        ('Начальное общее', 'Начальное общее'),
        ('Основное общее', 'Основное общее'),
        ('Среднее общее', 'Среднее общее'),
        ('Неполное высшее', 'Неполное высшее'),
        ('Высшее', 'Высшее'))
    library_card = models.CharField('Номер читательского билета', max_length=16)
    name = models.CharField('ФИО', max_length=200)
    passport_number = models.CharField('Номер паспорта', max_length=12)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=200)
    phone = models.CharField('Номер телефона', max_length=13)
    education = models.CharField('Образование', choices=education_type, max_length=50)
    academic = models.BooleanField('Наличие ученой степени', default=False)

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField('Название места чтения', max_length=50)
    capacity = models.IntegerField('Вместимость', blank=True, null=True)

    class Meta:
        verbose_name = "Место чтения"
        verbose_name_plural = "Места чтения"

    def __str__(self):
        return self.name


class Fix(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Читатель')
    date_fix = models.DateField('Дата закревления', auto_now_add=True)
    handed = models.BooleanField('Книга сдана', default=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место чтения', related_name='place_fix')

    class Meta:
        verbose_name = "Закрепление книги"
        verbose_name_plural = "Закрепления книг"

    def __str__(self):
        return ""+str(self.reader.library_card)+" ("+self.book.name+")"








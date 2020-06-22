from django.db import models
# from django.contrib.auth.models import User


class Hall(models.Model):
    name = models.CharField(max_length=14, verbose_name="название")
    capacity = models.SmallIntegerField(verbose_name="вместимость (человек)")

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return "Зал "+str(self.id)+" ("+self.name+")"


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="название")
    author = models.CharField(max_length=100, verbose_name="автор(ы)")
    publisher = models.CharField(max_length=50, verbose_name="издатель")
    edition_year = models.SmallIntegerField(verbose_name="год издания")
    sphere = models.CharField(max_length=30, verbose_name="раздел")
    cipher = models.CharField(max_length=20, verbose_name="шифр книги")
    receipt_date = models.DateField(verbose_name="дата поступления")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="зал")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return 'единица №'+str(self.id)+' экземпляр книги "'+self.title+'"'+' №'+self.cipher[-1]


class Reader(models.Model):
    EdType = (
        ('среднее общее', 'среднее общее'),
        ('среднее профессиональное', 'среднее профессиональное'),
        ('неполное высшее', 'неполное высшее'),
        ('бакалавр', 'бакалавр'),
        ('специалист', 'специалист'),
        ('магистр', 'магистр'),
        ('аспирантура', 'аспирантура'))
    library_card_num = models.CharField(max_length=8, verbose_name="номер читательского билета")
    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    passport_data = models.CharField(max_length=10, verbose_name="серия, номер паспорта")
    birth_date = models.DateField(verbose_name="дата рождения")
    home_address = models.TextField(verbose_name="адрес")
    phone_num = models.CharField(max_length=12, verbose_name="контактный номер")
    education = models.CharField(choices=EdType, max_length=24, verbose_name="образование")
    degree = models.BooleanField(verbose_name="наличие учёной степени")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="зал")
    books = models.ManyToManyField(Book, through='Attachment', verbose_name="книги", related_name='attached_book')

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return 'читатель '+self.full_name+', билет №'+self.library_card_num


class Attachment(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="читатель")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")
    attachment_starting_date = models.DateField(verbose_name="время закрепления")
    attachment_finishing_date = models.DateField(null=True, blank=True, verbose_name="время открепления")

    class Meta:
        verbose_name = "Закрепление"
        verbose_name_plural = "Закрепления"

    def __str__(self):
        return 'закрепление №'+str(self.id)+', '+str(self.book)+', '+str(self.reader)


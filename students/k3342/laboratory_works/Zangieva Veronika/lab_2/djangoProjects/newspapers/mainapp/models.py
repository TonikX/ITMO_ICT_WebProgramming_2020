from django.db import models

class PostOffice(models.Model):
	poNum = models.PositiveIntegerField('Номер почтового отделения')
	poAddress = models.CharField('Адрес почтового отделения', max_length = 500)


class PrintingHouse(models.Model):
	CType = (
		('открыта', 'открыта'),
		('закрыта', 'закрыта'),
	)
	phName = models.CharField('Название типографии', max_length = 50)
	phAddress = models.CharField('Адрес типографии', max_length = 500)
	phWorkStatus = models.CharField('Статус', choices=CType, max_length=100)


class Newspaper(models.Model):
	npName = models.CharField('Название газеты', max_length = 50)
	npEditorName = models.CharField('ФИО редактора', max_length = 100)
	npEditionIndex = models.IntegerField('Индекс издания')
	npPrice = models.PositiveIntegerField('Цена экземпляра')


class Order(models.Model):
	oPoCode = models.ForeignKey(PostOffice, on_delete=models.CASCADE, verbose_name='Почтовое отделение')
	oNpCode = models.ForeignKey(Newspaper, on_delete=models.CASCADE, verbose_name='Газета',)
	oNpCount = models.IntegerField('Количество экземпляров')


class PrintRun(models.Model):
	prPoCode = models.ForeignKey(PostOffice, on_delete=models.CASCADE)
	prOCode = models.ForeignKey(Order, on_delete=models.CASCADE)
	prNpCode = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
	prPhCode = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE)
	prPrintRun = models.PositiveIntegerField('Тираж')



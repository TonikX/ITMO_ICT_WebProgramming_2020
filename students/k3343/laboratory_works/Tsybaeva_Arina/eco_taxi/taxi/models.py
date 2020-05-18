from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Client(models.Model):
    """Клиент"""
    name = models.CharField("ФИО", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    email = models.EmailField("Email")
    telephone = models.CharField("Телефон", max_length=15)
    address = models.TextField("Адрес", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Driver(models.Model):
    name = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    email = models.EmailField("Email")
    telephone = models.CharField("Телефон", max_length=15)
    car_model = models.CharField("Модель и марка машины", max_length=30)
    car_number = models.CharField("Номер машины", max_length=10)
    image = models.ImageField("Изображение", upload_to="drivers/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"


class Order(models.Model):
    driver = models.ForeignKey("Driver", verbose_name="Водитель", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", verbose_name="Мусор")
    mass = models.FloatField("Масса мусора в кг")
    cost = models.IntegerField()
    complete = models.BooleanField("Исполнен", default=True)
    data = models.DateField("Дата", default=datetime.date.today)

    def __str__(self):
        return f"{self.driver} - {self.client}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Storage(models.Model):

    order = models.ManyToManyField("Order", verbose_name="Заказ: ")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Склад"



from django.db import models
from django.contrib.auth.models import User


class Human(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    human_surname = models.CharField("Фамилия", max_length=20)
    human_name = models.CharField("Имя", max_length=20)
    human_patronym = models.CharField("Отчество", max_length=20)
    human_passport = models.CharField("Паспорт", max_length=10)
    org = models.BooleanField(default=False)


class Dogs(models.Model):
    dog_owner = models.ForeignKey(Human, on_delete=models.CASCADE)
    dog_club = models.CharField("Клуб", max_length=20, null=True)
    dog_name = models.CharField("Кличка", max_length=20)
    dog_breed = models.CharField("Порода", max_length=20)
    dog_age = models.CharField("Возраст", max_length=10)
    dog_class = models.CharField("Классность", max_length=20)
    dog_document = models.CharField("Номер документа", max_length=20)
    dog_mother = models.CharField("Кличка матери", max_length=20)
    dog_father = models.CharField("Кличка отца", max_length=20)
    dog_vaccination = models.DateField("Дата последней прививки")

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.dog_name


class Experts(models.Model):
    expert_surname = models.CharField("Фамилия эксперта", max_length=20)
    expert_name = models.CharField("Имя эксперта", max_length=20)
    expert_club = models.CharField("Клуб эксперта", max_length=20)

    class Meta:
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"

    def __str__(self):
        return self.expert_surname


class Funders(models.Model):
    funder_name = models.CharField("ФИО или компания", max_length=20)

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"

    def __str__(self):
        return self.funder_name


class Rings(models.Model):
    ring_number = models.CharField("Номер ринга", max_length=10)

    class Meta:
        verbose_name = "Ринг"
        verbose_name_plural = "Ринги"

    def __str__(self):
        return self.ring_number


class Shows(models.Model):
    show_presentment = models.CharField("Описание выставки", max_length=20)

    class Meta:
        verbose_name = "Выставка"
        verbose_name_plural = "Выставки"

    def __str__(self):
        return self.show_presentment


class Records(models.Model):
    record_show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    record_dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)
    record_medical = models.BooleanField("медосмотр", default=False)
    record_pay = models.BooleanField("оплата счёта", default=False)
    record_confirmation = models.BooleanField("Подтверждение", default=False)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Acts(models.Model):
    SCORES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    act_show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    act_dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)
    act_ring = models.ForeignKey(Rings, on_delete=models.CASCADE)
    act_1 = models.CharField("упражнение 1", max_length=1, choices=SCORES)
    act_2 = models.CharField("упражнение 2", max_length=1, choices=SCORES)
    act_3 = models.CharField("упражнение 3", max_length=1, choices=SCORES)

    class Meta:
        verbose_name = "Выступление"
        verbose_name_plural = "Выступления"


class Sponsors(models.Model):
    sponsor_funder = models.ForeignKey(Funders, on_delete=models.CASCADE)
    sponsor_show = models.ForeignKey(Shows, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Спонсирование"
        verbose_name_plural = "Спонсирования"


class Judgings(models.Model):
    judging_show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    judging_expert = models.ForeignKey(Experts, on_delete=models.CASCADE)
    judging_ring = models.ForeignKey(Rings, on_delete=models.CASCADE)
    judging_confirmation = models.BooleanField("Подтверждение", default=False)

    class Meta:
        verbose_name = "Судейство"
        verbose_name_plural = "Судейства"

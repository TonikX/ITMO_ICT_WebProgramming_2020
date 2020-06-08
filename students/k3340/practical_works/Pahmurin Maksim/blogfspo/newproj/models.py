from django.db import models


class Automobile(models.Model):
    mark = models.CharField(max_length=30)
    model_car = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    nomber = models.IntegerField()


class Autoholder(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    holders = models.ManyToManyField(Automobile, through='Holding')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class AdditionalData(models.Model):
    owner = models.OneToOneField(Autoholder, on_delete=models.CASCADE, primary_key=True)
    passport_num = models.CharField(max_length=50)
    home_address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)


class Holding(models.Model):
    holder = models.ForeignKey(Autoholder, on_delete=models.CASCADE)
    auto = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    start_holding = models.DateField()
    end_holding = models.DateField()


class Drivers_license(models.Model):
    CHOICES = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    lisence_number = models.IntegerField
    lisence_date = models.DateField()
    lisense_type = models.CharField(max_length=1, choices=CHOICES)
    lisense_holder = models.ForeignKey(Autoholder, on_delete=models.CASCADE)

from django.db import models


class CarOwner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'User {self.name}'


class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    state_number = models.PositiveIntegerField()
    owned_by = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_brand}'


class DriverLicense(models.Model):
    TYPE_CHOICES = (('A', 'Bike'),
                    ('B', 'Light Rigid'),
                    ('C', 'Medium Rigid'),
                    ('D', 'Heavy Rigid'),
                    ('E', 'Heavy Combination'))

    license_id = models.PositiveIntegerField()
    date_of_issue = models.DateField(blank=True, null=True)
    choice_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    owner = models.ManyToManyField(Car, through='TemporaryOwner', related_name='temp_owner')

    def __str__(self):
        return f'{self.license_id}'


class TemporaryOwner(models.Model):
    car_owner = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Car')
    driver_license = models.ForeignKey(DriverLicense, on_delete=models.CASCADE)
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.car_owner} owned by user with license id {self.driver_license}'
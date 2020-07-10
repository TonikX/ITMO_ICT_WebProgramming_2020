from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name


class Mountain(models.Model):
    mountain_name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.CharField(max_length=30)
    height = models.IntegerField()

    class Meta:
        db_table = 'Mountain'

    def __str__(self):
        return self.mountain_name


class Club(models.Model):
    club_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)

    class Meta:
        db_table = 'Club'

    def __str__(self):
        return self.club_name


class Alpinist(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(default='1980-01-01')
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=150, default='city-street-house-flat', blank=True)

    class Meta:
        db_table = 'Alpinist'

    def __str__(self):
        return self.name


class Group(models.Model):

    SUCCESS_STATUS_GROUP = (
        ('Finished', 'Ascent was successfully finished'),
        ('Not finished', 'Ascent was not finished'),
        ('Not started', 'Ascent was not started')
    )

    group_code = models.CharField(max_length=30)
    participant = models.ManyToManyField(Alpinist)
    contact_person = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    group_success = models.CharField(max_length=30, choices=SUCCESS_STATUS_GROUP)

    class Meta:
        db_table = 'Group'

    def __str__(self):
        return self.group_code


class IndSuccess(models.Model):

    SUCCESS_STATUS_IND = (
        ('Finished', 'Ascent was successfully finished'),
        ('Injured', 'Ascent was not finished due to the injury'),
        ('Not finished', 'Ascent was not finished on behalf of the alpinist'),
        ('Not started', 'Alpinist did not participate')
    )

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    participant = models.ForeignKey(Alpinist, on_delete=models.CASCADE)
    individual_success = models.CharField(max_length=30, choices=SUCCESS_STATUS_IND)

    class Meta:
        db_table = 'IndSuccess'
        verbose_name = 'Individual success'
        verbose_name_plural = 'Individual successes'


class Ascent(models.Model):
    ascent_code = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    duration = models.DurationField()
    complexity = models.IntegerField(default=5)
    ascent_height = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'Ascent'

    def __str__(self):
        return self.ascent_code


class Emergency(models.Model):

    EMERGENCY_SITUATION = (
        ('Injury', 'Alpinist was injured'),
        ('Gone', 'Alpinist got lost'),
        ('Death', 'Alpinist died')
    )

    participant = models.ForeignKey(Alpinist, on_delete=models.CASCADE)
    ascent = models.ForeignKey(Ascent, on_delete=models.CASCADE)
    date = models.DateField()
    situation = models.CharField(max_length=10, choices=EMERGENCY_SITUATION)
    commentary = models.TextField(max_length=1000)

    class Meta:
        db_table = 'Emergency'
        verbose_name_plural = 'Emergencies'

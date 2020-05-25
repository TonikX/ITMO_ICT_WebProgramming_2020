from django.db import models

# Create your models here.


class Club(models.Model):
    club_name = models.CharField(max_length=25)
    town_club = models.CharField(max_length=25)

    def __srt__(self):
        return self.club_name


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    town = models.CharField(max_length=25)
    passport = models.CharField(max_length=25)
    expert_choice = [
        ('exp', 'expert'),
        ('part', 'participant'),
    ]
    expert = models.CharField(max_length=4, choices=expert_choice)

    def __srt__(self):
        return self.last_name


class Dog(models.Model):
    dog_name = models.CharField(max_length=25)
    breed = models.CharField(max_length=25)
    age = models.CharField(max_length=10)
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=gender_choice)
    date_of_medicine = models.CharField(max_length=10)
    inspect_choice = [
        ('yes', 'everything is ok'),
        ('no', 'the dog is ill'),
    ]
    inspectation = models.CharField(max_length=3, choices=inspect_choice, default='no')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __srt__(self):
        return self.dog_name


class Show(models.Model):
    show_name = models.CharField(max_length=25)
    show_town = models.CharField(max_length=25)
    type_choice = [
        ('1', 'one breed'),
        ('not1', 'a lot of breeds'),
    ]
    type = models.CharField(max_length=4, choices=type_choice)
    start_date = models.DateField()
    end_date = models.DateField()

    def __srt__(self):
        return self.show_name


class Ring(models.Model):
    number = models.CharField(max_length=10)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ex1 = models.CharField(max_length=25)
    ex2 = models.CharField(max_length=25)
    ex3 = models.CharField(max_length=25)

    def __srt__(self):
        return self.number


class Registration(models.Model):
    num = models.CharField(max_length=10)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    fee_choice = [
        ('yes', 'fee paid'),
        ('no', 'not paid'),
    ]
    fee = models.CharField(max_length=3, choices=fee_choice,
                           default='no')

    def __srt__(self):
        return self.num


class Perform(models.Model):
    ring = models.ForeignKey(Ring, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class Grade(models.Model):
    expert = models.ForeignKey(User, on_delete=models.CASCADE)
    perform = models.ForeignKey(Perform, on_delete=models.CASCADE)
    points1 = models.CharField(max_length=5)
    points2 = models.CharField(max_length=5)
    points3 = models.CharField(max_length=5)


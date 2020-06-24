from django.db import models





# Create your models here.








class Owner(models.Model):


    first_name = models.CharField(max_length=50)


    last_name = models.CharField(max_length=50)


    date_birth = models.DateField()








class Car(models.Model):


    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


    name = models.CharField(max_length=30)


    type = models.CharField(max_length=50)


    colour = models.CharField(max_length=20)


    number = models.IntegerField








class Owning(models.Model):


    own_name = models.ForeignKey(Owner, on_delete=models.CASCADE)


    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)


    start_date = models.DateField()


    end_date = models.DateField()








class Passport(models.Model):


    TYPE_EX = (


        ('1', 'First'),


        ('2', 'Second'),


        ('3', 'Third'),


    )


    own_name = models.ForeignKey(Owner, on_delete=models.CASCADE)


    number = models.IntegerField


    start_date = models.DateField()


    type = models.CharField(max_length=10, choices=TYPE_EX)
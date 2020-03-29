from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.last_name

class Car(models.Model):
    CAR_COLOUR = (
        ('r', 'red'),
        ('o', 'orange'),
        ('y', 'yellow'),
        ('g', 'green'),
        ('b', 'blue'),
        ('p', 'purple'),
        ('pk', 'pink'),
        ('r', 'red'),
        ('bk', 'black'),
        ('gy', 'grey'),
        ('w', 'white'),
        ('bn', 'brown'),
        ('m', 'multicolour'),
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=2,choices=CAR_COLOUR)
    reg_plate = models.CharField(max_length=6)
    owned_by = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.model

class Driver_license(models.Model):
    TYPES = (
        ('A','A: motorcycle; tricycle; quadricycle; engine capacity<50cm^2; weight<400kg'),
        ('A1', 'A1: motorcycle; tricycle; weight<550kg'),
        ('B', 'B: car'),
        ('B1', 'B1: tricycle; quadricycle; weight<550kg, engine capacity<50cm^2'),
        ('C', 'C: truck; weight>3500kg; trailer<750kg'),
        ('C1', 'C1: truck; 3500<weight<7500kg; trailer<750kg'),
        ('D', 'D: passenger vehicle; trailer<750kg; seats>8'),
        ('D1', 'D1: passenger vehicle; trailer<750kg; 8<seats<16'),
        ('BE', 'BE: car with trailer'),
        ('CE', 'CE: truck; weight>3500kg; trailer>750kg'),
        ('C1E', 'C1E: truck; trailer>750kg; truck+trailer<12000kg'),
        ('DE', 'DE: passenger vehicle; trailer>750kg OR articulated bus'),
        ('D1E', 'D1E: bus not for passengers; trailer>750kg'),
        ('M', 'M: quadricycle; scooter; weight<350kg; engine capacity<50cm^2 '),
        ('Tm', 'Tm: tram'),
        ('Tb', 'Tb: trolleybus'),
    )
    number = models.CharField(max_length=10)
    date_given = models.DateField()
    type = models.CharField(max_length=3,choices=TYPES)
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField()

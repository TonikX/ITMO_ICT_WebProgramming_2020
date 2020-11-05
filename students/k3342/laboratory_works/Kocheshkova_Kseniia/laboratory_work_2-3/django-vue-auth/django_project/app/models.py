from django.db import models


class Visitor(models.Model):
    EDUCATION_CHOICES = (
        ('GP', 'General_preschool'),
        ('GI', 'General_initial'),
        ('GtM', 'General_the_main'),
        ('GtA', 'General_the_average'),
        ('PI', 'Professional_initial'),
        ('PtA', 'Professional_the_average'),
        ('PH', 'Professional_higher'),
        ('PP', 'Professional_postgraduate'),
        ('AG', 'Additional_general'),
        ('AP', 'Additional_professional'),
    )
    library_card_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    passport_ID = models.IntegerField()
    adress = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    academic_degree = models.BooleanField()
    data_last_registration = models.DateField()
    failure = models.BooleanField()
    
    def __str__(self):
        return self.library_card_number


class Book(models.Model):
    book_number = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    author_s = models.CharField(max_length=150)
    publishing_house = models.CharField(max_length=50)
    the_year_of_publishing = models.CharField(max_length=50)
    number_of_copies = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.book_number


class Hall(models.Model):
    hall_name = models.CharField(max_length=20)
    max_visitor = models.CharField(max_length=50)
    start_time_working = models.CharField(max_length=40)
    finish_time_working = models.CharField(max_length=40)
    weekend = models.CharField(max_length=50)
    
    def __str__(self):
        return self.hall_name


class Librarian(models.Model):
    passport = models.CharField(max_length=12)
    librarian_name = models.CharField(max_length=150)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.librarian_name


class Ownership(models.Model):
    visitor = models.ForeignKey('Visitor', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    start_of_owning = models.CharField(max_length=40)
    finish_of_owning = models.CharField(max_length=40)
    returning = models.CharField(max_length=40)


class Accessory(models.Model):
    visitor = models.ForeignKey('Visitor', on_delete=models.CASCADE)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    data_registration = models.DateField()


class Rent(models.Model):
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    librarian = models.ForeignKey('Librarian', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    type_event = models.CharField(max_length=50)
    max_people = models.IntegerField()
    data_time = models.DateTimeField()
    time_period = models.TimeField()

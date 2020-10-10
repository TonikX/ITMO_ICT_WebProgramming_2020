from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=121)
    founder = models.CharField(max_length=240)
    currDirector = models.CharField(max_length=240)
    #logo = models.ImageField()
    description = models.TextField()
    # name
    slug = models.SlugField(max_length=120, unique=True)


class Author(models.Model):
    fullName = models.CharField(max_length=240)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birth = models.DateField()
    death = models.DateField()
    # birth.year + lastName
    slug = models.SlugField(max_length=250, unique=True)
    #photo = models.ImageField()


class Book(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    authorID = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publishDate = models.DateField()
    mark = models.FloatField()
    #cover = models.ImageField()
    TYPE_COVER = (
        ('N', 'None'),
        ('S', 'Soft'),
        ('H', 'Hard'),
    )
    typeCover = models.CharField(max_length=1, choices=TYPE_COVER)
    # publishDate.Year + tittle.short
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


class Series(models.Model):
    title = models.CharField(max_length=120)
    books = models.ManyToManyField(Book, verbose_name="list of books")
    # title
    slug = models.SlugField(max_length=120, unique=True)

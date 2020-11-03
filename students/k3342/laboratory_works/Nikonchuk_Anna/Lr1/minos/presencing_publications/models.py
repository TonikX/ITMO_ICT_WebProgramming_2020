from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# from phonenumber_field.modelfields import PhoneNumberField
# model field reference https://docs.djangoproject.com/en/3.1/ref/models/fields/


LANGS = (
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('af', 'Afrikaans'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('as', 'Assamese'),
    ('ay', 'Aymara'),
    ('az', 'Azerbaijani'),
    ('ba', 'Bashkir'),
    ('be', 'Byelorussian'),
    ('bg', 'Bulgarian'),
    ('bh', 'Bihari'),
    ('bi', 'Bislama'),
    ('bn', 'Bengali'),
    ('bo', 'Tibetan'),
    ('br', 'Breton'),
    ('ca', 'Catalan'),
    ('co', 'Corsican'),
    ('cs', 'Czech'),
    ('cy', 'Welsh'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dz', 'Bhutani'),
    ('el', 'Greek'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('es', 'Spanish'),
    ('et', 'Estonian'),
    ('eu', 'Basque'),
    ('fa', 'Persian'),
    ('fi', 'Finnish'),
    ('fj', 'Fiji'),
    ('fo', 'Faroese'),
    ('fr', 'French'),
    ('fy', 'Frisian'),
    ('ga', 'Irish'),
    ('gd', 'Scots Gaelic'),
    ('gl', 'Galician'),
    ('gn', 'Guarani'),
    ('gu', 'Gujarati'),
    ('ha', 'Hausa'),
    ('he', 'Hebrew'),
    ('iw', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('hy', 'Armenian'),
    ('ia', 'Interlingua'),
    ('id', 'Indonesian'),
    ('in', 'Indonesian'),
    ('ie', 'Interlingue'),
    ('ik', 'Inupiak'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('iu', 'Inuktitut'),
    ('ja', 'Japanese'),
    ('jw', 'Javanese'),
    ('ka', 'Georgian'),
    ('kk', 'Kazakh'),
    ('kl', 'Greenlandic'),
    ('km', 'Cambodian'),
    ('kn', 'Kannada'),
    ('ko', 'Korean'),
    ('ks', 'Kashmiri'),
    ('ku', 'Kurdish'),
    ('ky', 'Kirghiz'),
    ('la', 'Latin'),
    ('ln', 'Lingala'),
    ('lo', 'Laotian'),
    ('lt', 'Lithuanian'),
    ('lv', 'Latvian'),
    ('lv', 'Lettish'),
    ('mg', 'Malagasy'),
    ('mi', 'Maori'),
    ('mk', 'Macedonian'),
    ('ml', 'Malayalam'),
    ('mn', 'Mongolian'),
    ('mo', 'Moldavian'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('mt', 'Maltese'),
    ('my', 'Burmese'),
    ('na', 'Nauru'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch'),
    ('no', 'Norwegian'),
    ('oc', 'Occitan'),
    ('om', 'Oromo'),
    ('or', 'Oriya'),
    ('pa', 'Pundjabi'),
    ('pl', 'Polish'),
    ('ps', 'Pashto'),
    ('pt', 'Portuguese'),
    ('qu', 'Quechua'),
    ('rm', 'Rhaeto-Romance'),
    ('rn', 'Kirundi'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('rw', 'Kiyarwanda'),
    ('sa', 'Sanskrit'),
    ('sd', 'Sindhi'),
    ('sg', 'Sangho'),
    ('sh', 'Serbo-Croatian'),
    ('si', 'Singhalese'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('sm', 'Samoan'),
    ('sn', 'Shona'),
    ('so', 'Somali'),
    ('sq', 'Albanian'),
    ('sr', 'Serbian'),
    ('ss', 'Siswati'),
    ('st', 'Sesotho'),
    ('su', 'Sudanese'),
    ('sv', 'Swedish'),
    ('sw', 'Swahili'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('th', 'Thai'),
    ('ti', 'Tigrinya'),
    ('tk', 'Turkmen'),
    ('tl', 'Tagalog'),
    ('tn', 'Setswana'),
    ('to', 'Tonga'),
    ('tr', 'Turkish'),
    ('ts', 'Tsonga'),
    ('tt', 'Tatar'),
    ('tw', 'Twi'),
    ('ug', 'Uigur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('vi', 'Vietnamese'),
    ('vo', 'Volapuk'),
    ('wo', 'Wolof'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('ji', 'Yiddish'),
    ('yo', 'Yorouba'),
    ('za', 'Zhuang'),
    ('zh', 'Chinese'),
    ('zu', 'Zulu'),
)

COVER_TYPE = (
    ('NC', 'None cover'),
    ('SC', 'Soft cover'),
    ('PB', 'Paperback'),
    ('OC', 'Ordinary'),
    ('HC', 'Hard cover'),
    ('AC', 'Audio CD'),
    ('AB', 'Audiobook'),
    ('AA', 'Audible Audio'),
    ('EB', 'Ebook'),
    ('KE', 'Kindle Edition'),
)

USER_TYPE = (  
    ('A', 'Author'),
    ('M', 'Admin'),
    ('P', 'Publisher'),
    ('S', 'Book Shop'),
    ('U', 'User')
)

IMPORTANCE_TYPES = (
        ('UI', 'Urgent and important'),
        ('NI', 'Not urgent and important'),
        ('NN', 'Not urgent and not important'),
        ('IB', 'I am bored')
    )

COMMENT_TYPE = (
    ('A', 'Author'),
    ('B', 'Book'),    
    ('P', 'Publisher'),
    ('S', 'Shop')
)


class UserProfile(models.Model):
    isu = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    type_user = models.CharField(max_length=2, choices=USER_TYPE, blank=True, null=True)
    photo = models.ImageField(upload_to='users', blank=True, null=True)
    uniq_num = models.IntegerField(unique=True, blank=True, null=True)
    location = models.CharField(max_length=300, unique=True, blank=True, null=True)
    nationality = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        first_name = self.first_name
        last_name = self.last_name
        type_user = self.get_type_user_display
        return type_user + ' ' + first_name + ' ' + last_name


class Director(models.Model):
    full_name = models.CharField(max_length=240)
    short_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return self.short_name + ' (' + str(self.id) + ')'


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    full_another_name = models.CharField(max_length=240, blank=True, null=True)
    parent = models.CharField(max_length=300, blank=True, null=True)
    founder = models.CharField(max_length=300, blank=True, null=True)
    foundation_date = models.DateField(blank=True, null=True)
    director = models.ManyToManyField(Director, through='DirectorDuties', blank=True)
    p_slug = models.SlugField(max_length=120, unique=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    fact_address = models.CharField(max_length=240, blank=True, null=True)
    city: str = models.CharField(max_length=180, blank=True, null=True)
    ''' The max length title of the city is a Bangkok: "Krungthepmahanakhon 
    Amonrattanakosin Mahintharayutthaya Mahadilokphop Noppharatratchathaniburirom 
    Udomratchaniwetmahasathan Amonphimanawatansathit Sakkathattiyawitsanukamprasit" 
    = 176 symbols '''
    country = models.CharField(max_length=60, blank=True, null=True)
    ''' The max length title on the country is a 
    "United Kingdom of great Britain and Northern Ireland" '''
    distribution = models.CharField(max_length=300, blank=True, null=True)
    about = models.TextField(max_length=2000, blank=True, null=True)
    logo = models.ImageField(upload_to='publishers', blank=True, null=True)
    who_load = models.CharField(max_length=120, default='Admin')

    def __str__(self):
        # return '{}'.format(self.name + '(' + str(self.id) + ')')
        return format(self.name)


class DirectorDuties(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    place = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    """ performed duties period """
    date_begin = models.DateField(blank=True, null=True)
    date_left = models.DateField(blank=True, null=True)


class Author(models.Model):
    full_name = models.CharField(max_length=1500)
    ''' the world's longest human name consists of 0,478 letters '''
    short_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)  # for anonymous
    death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='authors', blank=True, null=True)
    a_slug = models.SlugField(max_length=120, unique=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    career = models.CharField(max_length=300, blank=True, null=True)
    direction = models.CharField(max_length=300, blank=True, null=True)
    a_ganre = models.CharField(max_length=300, blank=True, null=True)
    who_load = models.CharField(max_length=120, default='Admin')

    def __str__(self):
        return '{}'.format(self.short_name + '(' + str(self.id) + ')')


class Book(models.Model):
    orig_lang_title = models.CharField(max_length=120, db_index=True, verbose_name='Original language title')
    orig_lang = models.CharField(max_length=2, choices=LANGS, verbose_name='Original language')
    trans_lang = models.CharField(max_length=2, choices=LANGS, blank=True, null=True,
                                  verbose_name='Translation language')
    title = models.CharField(max_length=120, blank=True, null=True)
    editor = models.CharField(max_length=300, blank=True, null=True)
    translator = models.CharField(max_length=300, blank=True, null=True)
    narrator = models.CharField(max_length=300, blank=True, null=True)
    illustrator = models.CharField(max_length=300, blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    type_cover = models.CharField(max_length=2, choices=COVER_TYPE, blank=True, null=True)
    cover = models.ImageField(upload_to='books', blank=True, null=True)
    b_slug = models.SlugField(verbose_name='Slug')
    b_ganre = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ganre')
    descr = models.TextField(verbose_name='description', blank=True, null=True)
    who_load = models.CharField(max_length=120, default='Admin')

    def __str__(self):
        return self.b_slug + '_' + self.authors

    def __unicode__(self):
        return self.b_slug


class Series(models.Model):
    title = models.CharField(max_length=139)
    books = models.ManyToManyField(Book, blank=True)
    publisher: Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True)
    type_cover = models.CharField(max_length=2, choices=COVER_TYPE, blank=True, null=True)
    mockup = models.ImageField(upload_to='series', blank=True)
    series_slug = models.SlugField(verbose_name='Slug')


class Shelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    books = models.ManyToManyField(Book, blank=True, null=True)
    shelf_slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.title + ' (' + str(self.id) + ')'


class Shop(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=60, blank=False, null=False)
    location = models.CharField(max_length=600, unique=True)
    # phone = PhoneNumberField(unique=True, blank=False, null=False)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    website = models.URLField(unique=True, blank=False, null=False)
    open_time = models.TimeField(blank=True, null=True)
    close_time = models.TimeField(blank=True, null=True)
    shop_slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.location


class Stock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    serial_num = models.CharField(max_length=20)  # возможно стоит назначить вместо id

    def __str__(self):
        return self.serial_num


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Commentator')
    type = models.CharField(max_length=2, choices=COMMENT_TYPE, blank=True, null=True)
    place_author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    place_book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    place_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    place_shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    importance = models.CharField('Importance', max_length=2, choices=IMPORTANCE_TYPES, blank=True, null=True)
    content = models.CharField(max_length=600)
    comment_date = models.DateTimeField('Date', auto_now_add=True)

    def __int__(self):
        return self.id

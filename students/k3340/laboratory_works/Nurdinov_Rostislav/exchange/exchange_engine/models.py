from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.urls import reverse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, username: str, password: str):
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_user(self, username: str, password: str):
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
    )

    is_superuser = models.BooleanField(
        'is_superuser',
        default=False
    )

    is_staff = models.BooleanField(
        'is_staff',
        default=False
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_birth = models.DateField(max_length=50)
    address = models.CharField(max_length=50)
    status_work = models.BooleanField()
    last_salary = models.IntegerField()

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.second_name)


class Profession(models.Model):
    RANK_TYPES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
    ]
    prof = models.CharField(max_length=50)
    max_rank = models.CharField(choices=RANK_TYPES, default='1', max_length=1)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return "{}".format(self.prof)


class Resume(models.Model):
    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]
    jobseeker = models.OneToOneField(JobSeeker, on_delete=models.CASCADE)
    education = models.CharField(choices=EDUCATION_TYPES, default='1', max_length=1)
    description = models.CharField(max_length=1000)


class Experience(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name_org = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date_start = models.DateField()
    date_end = models.DateField(null=True)

    def __str__(self):
        return "{}".format(self.name_org)


class Employer(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    firm = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {} : {}".format(self.surname, self.name, self.second_name, self.firm)


class Vacancy(models.Model):
    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]
    RANK_TYPES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
    ]
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    status = models.BooleanField()
    date_start = models.DateField()
    education = models.CharField(choices=EDUCATION_TYPES, default='1', max_length=1)
    rank = models.CharField(choices=RANK_TYPES, default='1', max_length=1)
    salary = models.IntegerField()
    min_exp = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Application(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True, null=True)

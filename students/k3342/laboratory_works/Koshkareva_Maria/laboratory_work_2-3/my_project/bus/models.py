from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField


class Bus(models.Model):
    TYPES = (
        (1,'very little'),
        (2,'little'),
        (3,'average'),
        (4,'big'),
        (5,'articulated')
    )

    reg_plate = models.CharField(max_length=6, unique=True)
    type = models.IntegerField(choices=TYPES)
    capacity = models.IntegerField(default=0,
                                   help_text='fills in based on "Type"')

    def save(self,*args,**kwargs):
        type_cap = [5, 40, 65, 90, 110]
        self.capacity = type_cap[self.type - 1]
        super(Bus,self).save(*args,**kwargs)

    def __str__(self):
        return self.reg_plate

    class Meta:
        verbose_name_plural = "Buses"


class Route(models.Model):
    num = models.IntegerField(unique=True)
    loc_start = models.CharField(max_length=100)
    loc_end = models.CharField(max_length=100)
    time_start = models.TimeField()
    time_end = models.TimeField()
    interval_min = models.IntegerField()
    circle_time_min = models.IntegerField()

    def __str__(self):
        return str(self.num)


class Driver(models.Model):
    CLASSES = (
        (3,3),(2,2),(1,1)
    )

    passport = models.CharField(max_length=10, unique=True)
    d_of_b = models.DateField(null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    job_class = models.IntegerField(choices=CLASSES)
    date_begin = models.DateField()
    work_exp = models.IntegerField(default=0,
                                   help_text='fills in based on "Date begin"')
    salary = models.IntegerField(default=0,
                                 help_text='fills in based on "Work exp" and "Job class"')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    #img = CharField(max_length = 400,null=True)

    def __str__(self):
        return str(self.passport)

    def save(self,*args,**kwargs):
        self.work_exp = int((datetime.datetime.now().date()-self.date_begin).days/365.25)

        if self.work_exp > 30:
            pre_salary = 65000
        elif self.work_exp == 0:
            pre_salary = 19000
        else:
            pre_salary = 19000 + self.work_exp//2 * 3000
        # 1 -- *1.2, 2 -- *1.1, 3 -- *1.07
        self.salary = pre_salary*(1+1/(5*self.job_class))
        super(Driver,self).save(*args,**kwargs)


class Schedule(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, default=4,
                            help_text="Don't change to get the driver's bus")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, default=3,
                              help_text="Don't change to get the driver's route")
    work_day = models.DateField(null=True)
    work_start = models.TimeField(null=True)
    work_end = models.TimeField(null=True)

    @property
    def driver_bus(self):
        return self.driver.bus

    @property
    def driver_route(self):
        return self.driver.route

    def save(self,*args,**kwargs):
        if self.bus.id == 4:
            self.bus = self.driver_bus
        if self.route.id == 3:
            self.route = self.driver_route
        super(Schedule, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.driver} {self.work_start}'


class Report(models.Model):
    REASON_LIST = (
        (0,"OK"),
        (1,'Broken bus'),
        (2,'Sick driver'),
        (3,'No driver'),
        (4,'Other'),
    )
    schedule_line = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    reason = models.IntegerField(choices=REASON_LIST,default=0)

    @receiver(post_save, sender=Schedule)
    def create_sch_report(sender, instance, created, **kwargs):
        if created:
            Report.objects.create(schedule_line=instance)

    @receiver(post_save, sender=Schedule)
    def save_sch_report(sender, instance, **kwargs):
        instance.report.save()


class Malfunction(models.Model):
    PIECE_LIST = (
        (1,'engine'),
        (2,'tyres'),
        (3,'oil filter'),
        (4,'lights'),
        (5,'turn signals'),
        (6,'steering wheel'),
        (7,'rear-view mirrors'),
        (8,'other'),
    )

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    date_start = models.DateField()
    #piece = MultiSelectField(choices=PIECE_LIST)
    piece = models.CharField(max_length=100)
    #piece_now = MultiSelectField(choices=PIECE_LIST, null=True, blank=True)
    piece_now = models.CharField(null=True, blank=True, max_length=100)
    date_close = models.DateField(null=True, blank=True)

    @property
    def busmal_piece(self):
        return self.piece

    def save(self, *args, **kwargs):
        if not self.pk:
            self.piece_now = self.busmal_piece
        if not self.piece_now:
            self.date_close = datetime.datetime.now().strftime("%Y-%m-%d")
        super(Malfunction, self).save(*args, **kwargs)

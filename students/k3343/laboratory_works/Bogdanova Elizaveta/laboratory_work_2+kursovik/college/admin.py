from django.contrib import admin
from .models import Faculty, Specialty, Enrollee, Application,EGE, EgeSubject, Attestat, AttestatSubject

admin.site.register(Faculty)
admin.site.register(Specialty)
admin.site.register(Enrollee)
admin.site.register(Application)
admin.site.register(EGE)
admin.site.register(EgeSubject)
admin.site.register(Attestat)
admin.site.register(AttestatSubject)
# Register your models here.

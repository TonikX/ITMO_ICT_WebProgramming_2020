from django.contrib import admin
from .models import Patient, Doctor, App_times, Schedule, Appointment, PriceList


class PatientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'birth_date', 'sex', 'phone', 'email')


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(App_times)
admin.site.register(Schedule)
admin.site.register(Appointment)
admin.site.register(PriceList)

from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientCard)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Price)
admin.site.register(Calendar)
admin.site.register(Cabinet)

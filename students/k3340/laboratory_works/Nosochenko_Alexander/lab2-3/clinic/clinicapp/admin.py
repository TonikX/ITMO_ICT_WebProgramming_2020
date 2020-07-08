from django.contrib import admin
from .models import *

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Medicalrecord)
admin.site.register(Scheduleofdoctors)
admin.site.register(Cabinet)
admin.site.register(Transactions)
admin.site.register(Reception)
admin.site.register(Reviews)


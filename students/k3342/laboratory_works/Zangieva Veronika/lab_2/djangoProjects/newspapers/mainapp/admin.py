from django.contrib import admin

from .models import PrintingHouse, PostOffice, Newspaper, Order, PrintRun


admin.site.register(PrintingHouse)
admin.site.register(PostOffice)
admin.site.register(Newspaper)
admin.site.register(Order)
admin.site.register(PrintRun)


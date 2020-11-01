from django.contrib import admin
from hotels_list.models import Hotels, Rooms, Reservations, Reviews

admin.site.register(Hotels)
admin.site.register(Rooms)


admin.site.register(Reservations)
admin.site.register(Reviews)
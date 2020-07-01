from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from flights.models import Airport, Client, Flight, Booking, Comment


class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'country', 'city')
    list_display_links = ('code', 'country', 'city')


class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'dep_airport', 'dep_time', 'dep_terminal',
                    'arr_airport', 'arr_time', 'arr_terminal', 'flight_type',
                    'gate')
    list_display_links = ('code', 'dep_airport', 'dep_time', 'dep_terminal',
                          'arr_airport', 'arr_time', 'arr_terminal', 'flight_type',
                          'gate')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('code', 'client', 'flight', 'date', 'ticket_type')
    list_display_links = ('code', 'client', 'flight', 'date', 'ticket_type')


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comment)
admin.site.register(Client)


class UserInline(admin.StackedInline):
    model = Client
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

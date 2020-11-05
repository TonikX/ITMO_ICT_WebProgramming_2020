from django.contrib import admin

from .models import Person
admin.site.register(Person)
from .models import Flight
admin.site.register(Flight)
from .models import Comment
admin.site.register(Comment)
from .models import Ticket
admin.site.register(Ticket)
from .models import Reservation
admin.site.register(Reservation)
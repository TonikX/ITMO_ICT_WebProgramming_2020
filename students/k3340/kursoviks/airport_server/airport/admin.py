from django.contrib import admin
from .models import Flight, AirCarrier, Crew, TransitLanding, Route, Plane, CrewCommander, SecondPilot, Steward, Navigator

admin.site.register(Flight)
admin.site.register(AirCarrier)
admin.site.register(Crew)
admin.site.register(TransitLanding)
admin.site.register(Route)
admin.site.register(Plane)
admin.site.register(CrewCommander)
admin.site.register(SecondPilot)
admin.site.register(Steward)
admin.site.register(Navigator)
# Register your models here.

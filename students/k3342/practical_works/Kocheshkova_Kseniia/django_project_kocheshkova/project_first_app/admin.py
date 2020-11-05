from django.contrib import admin
from .models import Owner
admin.site.register(Owner)
from .models import Car
admin.site.register(Car)
from .models import Ownership
admin.site.register(Ownership)
from .models import License
admin.site.register(License)

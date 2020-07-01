from django.contrib import admin

# Register your models here.

from .models import Car
admin.site.register(Car)

from .models import Owning
admin.site.register(Owning)

from .models import Passport
admin.site.register(Passport)

from .models import Owner
admin.site.register(Owner)

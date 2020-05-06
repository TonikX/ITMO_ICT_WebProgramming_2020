from django.contrib import admin

from .models import Autoholder

admin.site.register(Autoholder)

from .models import Automobile

admin.site.register(Automobile)

from .models import Holding

admin.site.register(Holding)

from .models import Drivers_license

admin.site.register(Drivers_license)


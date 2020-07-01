from django.contrib import admin
from .models import Owner
from .models import Auto
from .models import Ownership
from .models import OwnerLicense

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(OwnerLicense)


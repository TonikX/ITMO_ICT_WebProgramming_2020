from django.contrib import admin
from django.apps import apps
from .models import Owner, Auto, Ownership, Licence

#admin.site.register(Owner, Auto, Ownership, Licence)
# Register your models here.
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
from django import forms
from .models import *

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "name",
            "surname",
            "birthdate"
        ]

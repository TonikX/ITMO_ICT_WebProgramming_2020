from django import forms
from .models import CarOwner, Car


class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "first_name",
            "last_name",
            "birth_date",
        ]

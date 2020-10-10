from django import forms
from .models import CarOwner


class CarOwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
        ]

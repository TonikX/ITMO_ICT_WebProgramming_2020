from django import forms
from .models import CarOwner

class OwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner
        fields = [
            "name",
            "surname",
            "date_of_birth"
        ]
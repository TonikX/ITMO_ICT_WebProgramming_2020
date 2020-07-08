from django import forms
from .models import CarOwner, Car


class AddOwner(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "name",
            "surname",
            "birth_date",
            "passport",
            "address",
            "nationality",
        ]
from django import forms
from .models import AutoOwner, Automobile


class AutoOwnerForm(forms.ModelForm):
    class Meta:
        model = AutoOwner
        fields = [
            "owner_name",
            "owner_surname",
            "date_of_birth"
        ]

class AutomobileForm(forms.ModelForm):
    class Meta:
        model = Automobile
        fields = [
            "car_make",
            "car_model",
            "car_color",
            "id_car"
        ]

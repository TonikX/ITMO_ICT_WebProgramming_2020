from django import forms
from .models import Auto_owner, Automobile


class Auto_ownerForm(forms.ModelForm):
    class Meta:
        model = Auto_owner
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
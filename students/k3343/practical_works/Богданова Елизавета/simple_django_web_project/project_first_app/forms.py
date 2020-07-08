from django import forms
from .models import Car_owner, Car


class Car_ownerForm(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = [
            "owner_name",
            "owner_surname",
            "date_of_birth"
        ]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "car_make",
            "car_model",
            "car_color",
            "id_car"
        ]
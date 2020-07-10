from django import forms
from .models import Car



class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "car_make",
            "car_model",
            "car_color",
            "id_car"
        ]
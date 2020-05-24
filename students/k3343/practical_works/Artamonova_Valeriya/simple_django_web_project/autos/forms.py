from django import forms
from .models import Automobile



class AutomobileForm(forms.ModelForm):
    class Meta:
        model = Automobile
        fields = [
            "car_make",
            "car_model",
            "car_color",
            "id_car"
        ]
from django import forms
from .models import *


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "passport_data",
            "home_address",
            "nationality",
        ]

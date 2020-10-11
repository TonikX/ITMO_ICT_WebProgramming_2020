from django import forms
from .models import User as CarOwner


class CarOwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
            "passport",
            "address",
            "ethnicity"
        ]

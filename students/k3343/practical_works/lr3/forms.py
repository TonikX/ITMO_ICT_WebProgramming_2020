from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = [
            "name",
            "surname",
            "birth_date",
            "passport",
            "nationality"
        ]
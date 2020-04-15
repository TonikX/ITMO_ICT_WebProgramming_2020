from django import forms
from .models import Owner


class OwnersForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Owner
        # specify fields to be used
        fields = [
            "name",
            "surname",
            "birthdate"
        ]

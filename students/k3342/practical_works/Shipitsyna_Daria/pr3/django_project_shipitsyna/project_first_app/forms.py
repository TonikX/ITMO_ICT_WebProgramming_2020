from django import forms
from .models import Car
from .models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]
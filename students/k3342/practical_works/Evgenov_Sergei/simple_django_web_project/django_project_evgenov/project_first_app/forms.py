from django import forms
from project_first_app.models import CarOwner


class OwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]

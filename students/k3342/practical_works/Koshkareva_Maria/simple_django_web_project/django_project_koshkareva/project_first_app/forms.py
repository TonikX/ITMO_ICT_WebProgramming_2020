from django import forms
from .models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["person","first_name","last_name","date_of_birth"]


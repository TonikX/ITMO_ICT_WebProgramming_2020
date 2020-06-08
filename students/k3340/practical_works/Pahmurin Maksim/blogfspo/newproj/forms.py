from django import forms
from .models import Autoholder, Automobile


# creating a form
class HolderForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Autoholder

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "date_of_birth"
        ]
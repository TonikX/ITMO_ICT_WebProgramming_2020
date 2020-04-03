from django import forms
from .models import Driver


class NewDriverForm(forms.ModelForm):
	class Meta:
		model = Driver

		fields = ["name", "surname", "birthdate"]

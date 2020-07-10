from django import forms
from .models import User as Driver


class NewDriverForm(forms.ModelForm):
	class Meta:
		model = Driver

		fields = ["name", "surname", "birthdate", "passport", "home_address", "nationality"]

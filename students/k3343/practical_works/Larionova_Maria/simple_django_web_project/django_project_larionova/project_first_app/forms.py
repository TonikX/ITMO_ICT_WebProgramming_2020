from django import forms
from .models import Owner


class CreateOwner(forms.ModelForm):
	class Meta:
		model = Owner

		fields = [
			"name",
			"surname",
			"birthdate"
		]

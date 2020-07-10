from django import forms
from .models import User as Owner


class CreateOwner(forms.ModelForm):
	class Meta:
		model = Owner

		fields = [
			"name",
			"surname",
			"birthdate",
			"address",
			"nationality",
			"passport_number"
		]

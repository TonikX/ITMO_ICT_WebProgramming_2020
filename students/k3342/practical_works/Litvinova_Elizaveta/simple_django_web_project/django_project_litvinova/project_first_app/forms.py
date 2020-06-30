from django import forms
from .models import *


class AutoOwnerForm(forms.ModelForm):
	class Meta:
		model = AutoOwner
		fields = [
			"first_name",
			"last_name",
			"birthdate",
			"age",
			"gender"
		]

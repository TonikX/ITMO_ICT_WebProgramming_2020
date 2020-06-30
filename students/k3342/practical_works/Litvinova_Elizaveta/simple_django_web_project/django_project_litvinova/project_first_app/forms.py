from django import forms
from .models import *
from .models import User as AutoOwner


class AutoOwnerForm(forms.ModelForm):
	class Meta:
		model = AutoOwner
		fields = [
			"first_name",
			"last_name",
			"birthdate",
			"age",
			"gender",
			"nationality",
			"passport",
			"address"
		]

from django import forms
from .models import User as Owner


class NewOwnerForm(forms.ModelForm):
	class Meta:
		model = Owner
		fields = ["name", "surname", "birthdate", "passport_num", "nationality", "address"]

from django import forms
from project_first_app.models import Owner


class OwnerForm(forms.ModelForm):

	class Meta:
		model = Owner
		fields = "__all__"

from django import forms
from .models import FlightComments


class CommentForm(forms.ModelForm):
	class Meta:
		model = FlightComments
		fields = [
			"author",
			"com_type",
			"com_text"
		]

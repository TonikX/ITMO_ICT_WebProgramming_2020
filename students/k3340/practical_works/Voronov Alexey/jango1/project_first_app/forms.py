from django import forms
from django.views.generic.edit import CreateView
from .models import Person, Vehicle


class AddVehicle(CreateView):
    model = Vehicle
    fields = ["manufacturer", "model", "color", "vehicle_number"]
    template_name = "project_first_app/vehicle_form.html"


class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [
			"name",
			"second_name",
			"date"
		]
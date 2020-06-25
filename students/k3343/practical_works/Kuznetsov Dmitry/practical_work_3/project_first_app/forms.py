from django import forms

from .models import Owner, Car


class OwnerForm(forms.ModelForm):

    class Meta:

        model = Owner

        fields = [

            "first_name",

            "last_name",

            "date_birth",

        ]


        labels = {

            "first_name": ("Имя"),

            "last_name": ("Фамилия"),

            "date_birth": ("Дата рождения"),

        }


class CarForm(forms.ModelForm):

    class Meta:

        model = Car

        fields = [

            "name",

            "type",

            "colour",

            "number",

        ]


        labels = {

            "name": ("Марка"),

            "type": ("Модель"),

            "colour": ("Цвет автомобиля"),

            "number": ("Номер автомобиля"),


        }
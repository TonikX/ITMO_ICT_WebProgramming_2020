from django import forms
from .models import User, Avto


class OwnerForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "birthday_date",
            "passport",
            "address",
            "nationality",
        ]

        labels = {
            "first_name": ("Имя"),
            "last_name": ("Фамилия"),
            "birthday_date": ("Дата рождения"),
            "passport": ("Паспрорт"),
            "address": ("Адрес"),
            "nationality": ("Национальность"),
        }


class AvtoForm(forms.ModelForm):
    class Meta:
        model = Avto

        fields = [
            "mark",
            "model",
            "color",
            "number",
        ]

        labels = {
            "mark": ("Марка"),
            "model": ("Модель"),
            "color": ("Цвет автомобиля"),
            "number": ("Номер автомобиля"),
        }

from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, DateInput
from .models import Comment, Reservation


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            "name_flight",
            "registration_evaluation",
            "flight_evaluation",
            "personnel_assessment",
            "category",
            "comment",
            "departure_date"
        ]
        labels = {
            "registration_evaluation": ("Rate the comfortable of registration:"),
            "flight_evaluation": ("Rate the comfortable of flight:"),
            "personnel_assessment": ("Rate the professional personnel:"),
            "category": ("Specify the class you flew in:"),
            "comment": ("Your comment:"),
            "departure_date": ("Your departure date:")
        }
        widgets = {"comment": Textarea(attrs={'cols': 50, 'rows': 5}),
                   "departure_date": DateInput(attrs={'type': 'date'})}


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "name_flight",
            "full_name",
            "passport_number",
            "phone_number",
            "category",
            "row",
            "place",
            "date_of_departure"
        ]
        labels = {
            "full_name": ("Write your full name:"),
            "passport_number": ("Passport number:"),
            "phone_number": ("Phone number:"),
            "category": ("Specify the class:"),
            "row": ("Specify the row:"),
            "place": ("Specify the place:"),
            "date_of_departure": ("Specify the data:"),
        }
        widgets = {"date_of_departure": DateInput(attrs={'type': 'date'})}

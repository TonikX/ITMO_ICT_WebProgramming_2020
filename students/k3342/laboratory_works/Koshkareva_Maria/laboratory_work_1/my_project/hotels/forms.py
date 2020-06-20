from django.forms import ModelForm, Select, SelectDateWidget
from .models import Comment
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django import forms


class SignupForm(forms.Form):
    AGE_LIST = (
        (1, '0-10 y.o.'),
        (2, '10-20 y.o.'),
        (3, '20-30 y.o.'),
        (4, '30-40 y.o.'),
        (5, '40-50 y.o.'),
        (6, '50-60 y.o.'),
        (7, '60-70 y.o.'),
        (8, '70-80 y.o.'),
        (9, '80-90 y.o.'),
        (10, '90-... y.o'),
    )
    age = forms.ChoiceField(choices=AGE_LIST)
    country = CountryField().formfield()

    def signup(self, request, user):
        u_profile = user.profile
        u_profile.age = self.cleaned_data['age']
        u_profile.country = self.cleaned_data['country']
        user.save()
        u_profile.save()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('rating','tourist_kind','vacation_start','vacation_end','text')
        widgets = {
            'vacation_start': SelectDateWidget(years=range(2018, 2021)),
            'vacation_end': SelectDateWidget(years=range(2018, 2021)),
            'rating': Select,
            'tourist_kind': Select,
        }
        labels = {
            'vacation_start': _('Stayed from'),
            'vacation_end': _('Stayed till'),
            'text': _(''),
            'tourist_kind': _('Came as a')
        }

    def clean(self):
        cleaned_data = super().clean()
        vacation_start = cleaned_data.get("vacation_start")
        vacation_end = cleaned_data.get("vacation_end")

        if vacation_start and vacation_end:
            if vacation_end <= vacation_start:
                raise forms.ValidationError(
                    "Choose correct vacation dates")

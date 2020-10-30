from django import forms
from django.forms import ModelForm, Textarea
from .models import Flight, Comment, AviaCompany


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment_type",
            "text",
        ]

        labels = {
            "comment_type": "Выберите тип коментария",
            "text": "Введите свой комментарий",
        }

        widgets = {
            "text": Textarea(attrs={'cols': 70, 'rows': 10}),
        }
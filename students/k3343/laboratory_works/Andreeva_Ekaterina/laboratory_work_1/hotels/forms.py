from django import forms
from django.forms import Textarea
from .models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "rating",
            "text",
            "check_in",
            "check_out"
        ]

        labels = {
            "rating": "Поставьте отелю оценку",
            "check_in": "Дата заселения",
            "check_out": "Дата выселения",
            "text": "Введите свой комментарий",
        }

        widgets = {
            "text": Textarea(attrs={'cols': 70, 'rows': 10}),
        }
from django.forms import ModelForm, Textarea, DateInput
from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            "hotel",
            "start",
            "end",
            "rating",
            "comment",
        ]
        labels = {
            "hotel": ("Выберите отель:"),
            "start": ("Дата прибытия:"),
            "end": ("Дата отправления:"),
            "rating": ("Рейтинг отеля"),
            "comment": ("Коментарий:")
        }
        widgets = {"comment" : Textarea(attrs={'cols': 50, 'rows': 5}),
                   "start": DateInput(attrs={'type': 'date'}),
                   "end": DateInput(attrs={'type':'date'})}
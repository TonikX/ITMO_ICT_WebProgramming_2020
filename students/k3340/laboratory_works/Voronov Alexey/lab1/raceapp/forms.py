
# coding=utf-8
from django.forms import ModelForm
from .models import Comment, Race, Result


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'type')

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ('name', 'description')

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ('name', 'description', 'date', 'result', 'vehicle', 'driver', 'race')
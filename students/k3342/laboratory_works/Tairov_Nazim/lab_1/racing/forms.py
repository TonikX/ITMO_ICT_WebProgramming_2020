from django import forms
from .models import Comment, RacerProfile


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('racer', 'comment_type', 'text')
        labels = {
            'comment_type': ('Choose the type of your comment'),
            'text': ('Enter your comment'),
        }


class RacerProfileForm(forms.ModelForm):
    class Meta:
        model = RacerProfile
        fields = '__all__'

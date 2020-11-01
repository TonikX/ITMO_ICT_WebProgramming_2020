from django.forms import ModelForm
from .models import Reviews


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = [
            "review_period",
            "review_rank",
            "review_text"
        ]

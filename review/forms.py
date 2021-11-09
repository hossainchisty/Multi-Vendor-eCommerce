from django.forms import ModelForm

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('star', 'reviewImage')

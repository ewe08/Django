from django import forms

from .models import Rating


class RatingForm(forms.ModelForm):
    """Form for rating based on model rating."""

    class Meta:
        model = Rating
        fields = (
            Rating.rate.field.name,
        )
        labels = {
            Rating.rate.field.name: 'Оценка',
        }
        help_texts = {
            Rating.rate.field.name: 'Оцените товар',
        }

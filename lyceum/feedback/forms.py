from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """Form for feedback based on model feedback."""

    class Meta:
        model = Feedback
        fields = (
            Feedback.text.field.name,
        )
        labels = {
            Feedback.text.field.name: 'Текст',
        }

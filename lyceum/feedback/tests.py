from django.test import Client, TestCase
from django.urls import reverse

from .forms import FeedbackForm
from .models import Feedback


class FormTests(TestCase):
    """Test form feedback."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_text_label(self):
        """Test correct text is in text_label"""

        text_label = FormTests.form.fields['text'].label
        self.assertEquals(text_label, 'Текст')

    def test_help_text_label(self):
        """Test correct text is in help_text_label."""

        help_text_label = FormTests.form.fields['text'].help_text
        self.assertEquals(help_text_label, 'Сюды текст надо для письма')

    def test_redirect_feedback(self):
        """Test redirect on feedback page."""

        form_data = {
            'text': 'Текст для теста',
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(response, reverse('feedback:feedback'))

    def test_add_feedback(self):
        """Test feedback add to the database."""

        feedbacks_count = Feedback.objects.count()

        form_data = {
            'text': 'Текст для теста',
        }
        Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(Feedback.objects.count(), feedbacks_count + 1)

    def test_form_show_correct(self):
        """Test that form showed correct"""
        response = Client().get(reverse('feedback:feedback'))

        self.assertIn(
            'form',
            response.context
        )

        self.assertEqual(
            response.context['form']['text'].label, 'Текст'
        )

        self.assertEqual(
            response.context['form']['text'].help_text,
            'Сюды текст надо для письма'
        )

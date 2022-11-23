from django.test import TestCase, Client
from django.urls import reverse

from .forms import FeedbackForm
from .models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_text_label(self):
        text_label = FormTests.form.fields['text'].label
        self.assertEquals(text_label, 'Текст')

    def test_help_text_label(self):
        help_text_label = FormTests.form.fields['text'].help_text
        self.assertEquals(help_text_label, 'Сюды текст надо для письма')

    def test_redirect_feedback(self):
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

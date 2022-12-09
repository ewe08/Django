from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import FeedbackForm
from .models import Feedback


class FeedbackView(FormView):
    """View class for feedback page.

    render feedback html.
    """
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
        """Create new feedback object and
        add it to database and send success emails."""

        text = form.cleaned_data['text']
        Feedback.objects.create(
            text=text,
        )
        send_mail(
            'Спасибо за ваш фидбек',
            f'{form.cleaned_data["text"]}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.TEST_USER_EMAIL],
            fail_silently=False,
        )
        send_mail(
            f'Отправлен фидбек от {settings.TEST_USER_EMAIL}',
            f'{form.cleaned_data["text"]}',
            settings.TEST_USER_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        :return: context with feedback form
        """
        context = super().get_context_data()
        context['title'] = 'Фидбэк'
        context['form'] = self.get_form()
        return context

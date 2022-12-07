from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import FeedbackForm
from .models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
        text = form.cleaned_data['text']
        Feedback.objects.create(
            text=text,
        )
        send_mail(
            'Тема письма',
            f'{form.cleaned_data["text"]}',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Фидбэк'
        context['form'] = self.get_form()
        return context

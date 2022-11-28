from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    template = 'feedback/feedback.html'
    form = FeedbackForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
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

        return redirect('feedback:feedback')

    context = {
        'title': 'Фидбэк',
        'form': form
    }
    return render(request, template, context)

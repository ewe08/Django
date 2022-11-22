from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import FeedbackForm


def feedback(request):
    template = 'feedback/feedback.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'title': 'Фидбэк',
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        send_mail(
            'Тема письма',
            f'{form.cleaned_data["text"]}',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return redirect('feedback:feedback')

    return render(request, template, context)

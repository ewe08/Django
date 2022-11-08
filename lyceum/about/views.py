from django.shortcuts import render


def description(request):
    return render(request, 'about/index.html', context={"title": 'О проекте'})

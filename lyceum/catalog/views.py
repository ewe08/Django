from django.shortcuts import render

from .models import Item


def item_list(request):
    context = {'title': 'Список', 'items': Item.objects.all()}
    return render(request, 'catalog/index_list.html', context=context)


def item_detail(request, pk: int):
    context = {'title': 'Подробнее', 'item': Item.objects.get(id=pk)}
    return render(request, 'catalog/index_detail.html', context=context)

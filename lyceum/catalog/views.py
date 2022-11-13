from django.shortcuts import render

from .models import Item, Photo


def item_list(request):
    context = {
        'title': 'Список',
        'items': Item.objects.all(),
    }
    return render(request, 'catalog/index_list.html', context=context)


def item_detail(request, pk: int):
    print(Photo.objects.filter(item_galery=pk))
    context = {'title': 'Подробнее',
               'item': Item.objects.get(id=pk),
               'photos': Photo.objects.filter(item_galery=pk)}
    return render(request, 'catalog/index_detail.html', context=context)

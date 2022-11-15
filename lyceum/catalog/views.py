from django.shortcuts import render, get_object_or_404

from .models import Item, Photo


def item_list(request):
    template = 'catalog/index_list.html'
    categories = dict()
    for item in Item.objects.published().order_by('category__name'):
        cat = item.category
        if cat in categories:
            categories[cat].append(item)
        else:
            categories[cat] = [item]

    context = {
        'title': 'Список',
        'categories': categories,
    }

    return render(request, template, context)


def item_detail(request, pk: int):
    template = 'catalog/index_detail.html'
    item = get_object_or_404(
        Item.objects.published(),
        pk=pk,
    )
    context = {'title': 'Подробнее',
               'item': item,
               'photos': Photo.objects.filter(item_galery=pk)}
    return render(request, template, context)

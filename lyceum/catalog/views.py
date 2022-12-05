from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Item, Photo


class ItemList(ListView):
    model = Item
    template_name = 'catalog/index_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Item.objects.categories()
        return {
            'title': 'Список',
            'categories': categories,
        }


class ItemDetail(DetailView):
    model = Item
    template_name = 'catalog/index_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Item.objects.published(),
            pk=self.kwargs['pk']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Подробнее'
        context['photos'] = Photo.objects.filter(
            item_galery=context['item'].id
        )
        return context

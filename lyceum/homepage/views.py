import pprint

from django.shortcuts import render
from catalog.models import Item
from django.views.generic import ListView


class HomeView(ListView):
    template_name = 'homepage/index.html'
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Главная'
        context['items'] = self.object_list
        return context

    def get_queryset(self):
        return Item.objects.published() \
            .filter(is_on_main=True) \
            .order_by('name')

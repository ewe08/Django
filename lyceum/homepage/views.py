from django.views.generic import ListView

from catalog.models import Item


class HomeView(ListView):
    template_name = 'homepage/index.html'
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Главная'
        context['items'] = self.object_list
        return context

    def get_queryset(self):
        return Item.objects.on_main()

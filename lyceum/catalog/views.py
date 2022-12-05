from django.shortcuts import render, redirect
from django.db.models import Avg
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Item, Photo
from rating.models import Rating
from rating.forms import RatingForm


class ItemList(ListView):
    model = Item
    template_name = 'catalog/index_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Item.objects.categories()
        return {
            'title': 'Список',
            'categories': categories,
        }


def item_detail(request, pk: int):
    template = 'catalog/index_detail.html'

    item = get_object_or_404(
        Item.objects.published(),
        pk=pk,
    )

    if request.user.is_authenticated:
        rating = Rating.objects.filter(item=item, user=request.user).first()
    else:
        rating = None

    if rating:
        user_rating = rating.rate
    else:
        user_rating = None

    count = Rating.objects.filter(item=pk).count()
    average_rating = Rating.objects.filter(item=pk).aggregate(Avg('rate'))
    form = RatingForm(request.POST or None, instance=rating)
    context = {'title': 'Подробнее',
               'item': item,
               'photos': Photo.objects.filter(item_galery=pk),
               'rating_count': count,
               'average_rating': average_rating['rate__avg'],
               'btn_label': 'Отправить',
               'user_rating': user_rating,
               'form': form}

    if request.method == 'POST' and form.is_valid():
        if rating:
            rating.rate = form.cleaned_data['rate']
        else:
            rating = Rating.objects.create(
               user=request.user,
               item=item,
               rate=form.cleaned_data['rate']
            )
        rating.save()

        return redirect(reverse('catalog:item_detail', args=[pk]))

    return render(request, template, context)


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

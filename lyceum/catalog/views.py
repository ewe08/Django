from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from rating.forms import RatingForm
from rating.models import Rating
from .models import Item, Photo


class ItemList(ListView):
    model = Item
    template_name = 'catalog/index_list.html'

    def get_queryset(self):
        queryset = Item.objects.categories()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список'
        return context


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
        rating = Rating.objects.filter(item=self.object,
                                       user=self.request.user.id).first()
        user_rating = rating.rate if rating else None
        count = Rating.objects.filter(item=self.kwargs['pk']).count()
        average_rating = Rating.objects.filter(
            item=self.kwargs['pk']
        ).aggregate(Avg('rate'))
        context['rating_count'] = count
        context['average_rating'] = average_rating['rate__avg']
        context['btn_label'] = 'Отправить'
        context['user_rating'] = user_rating
        context['form'] = RatingForm(instance=rating)
        return context

    def post(self, request, *args, **kwargs):
        form = RatingForm(request.POST)
        if not form.is_valid():
            return redirect(reverse('catalog:item_detail',
                                    args=[self.kwargs['pk']]))
        item = self.get_object()
        rating = Rating.objects.filter(item=item,
                                       user=request.user.id).first()
        if rating:
            rating.rate = form.cleaned_data['rate']
        else:
            rating = Rating.objects.create(
                user=request.user,
                item=item,
                rate=form.cleaned_data['rate']
            )
        rating.save()

        return redirect(reverse('catalog:item_detail',
                                args=[self.kwargs['pk']]))

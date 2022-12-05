from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.urls import reverse

from .models import Item, Photo
from rating.models import Rating
from rating.forms import RatingForm


def item_list(request):
    template = 'catalog/index_list.html'
    categories = Item.objects.categories()
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

    rating = Rating.objects.filter(item=item, user=request.user).first()
    if rating:
        user_rating = rating.rate
    else:
        user_rating = None
    count = Rating.objects.filter(item=pk).count()
    average_rating = Rating.objects.filter(item=pk).aggregate(Avg('rate'))['rate__avg']
    form = RatingForm(request.POST or None, instance=rating)
    context = {'title': 'Подробнее',
               'item': item,
               'photos': Photo.objects.filter(item_galery=pk),
               'rating_count': count,
               'average_rating': average_rating,
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

from django.db import models

from . import models as local_models


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(
                    is_published=True,
                    category__is_published=True,
                    )
                .select_related(
                    'category',
                    )
                .prefetch_related(
                    models.Prefetch(
                        'tags',
                        queryset=local_models.Tag.objects.published(),
                    )
                )
        )

    def categories(self):
        categories = dict()
        for item in (local_models.Item.objects
                     .published()
                     .order_by('category__name')):
            cat = item.category
            if cat in categories:
                categories[cat].append(item)
            else:
                categories[cat] = [item]
        return categories

    def on_main(self):
        return (local_models.Item.objects.published()
                .filter(is_on_main=True)
                .order_by('name'))


class TagManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .only('name')
        )

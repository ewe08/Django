from django.db import models

from . import models as local_models


class ItemManager(models.Manager):
    """Manager for item objects."""

    def published(self):
        """
        :return: all published objects with published category and tags
        """
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
        """
        :return: dictionary with categories like a key and
        items with this category like a value
        """
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
        """
        :return: all published items should be on main page
        """
        return (local_models.Item.objects.published()
                .filter(is_on_main=True)
                .order_by('name'))


class TagManager(models.Manager):
    """Manager for tag objects."""

    def published(self):
        """
        :return: all tags objects
        """
        return (
            self.get_queryset()
            .filter(is_published=True)
            .only('name')
        )

from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Tag, Item


class ItemListTest(TestCase):
    def tearDown(self):
        Item.objects.all().delete()
        super().tearDown()

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(name='Test Category',
                                               slug='test-category-slug',
                                               is_published=True, weight=50)
        cls.tag = Tag.objects.create(name='Test tag', is_published=True,
                                     slug='test-tag-slug')

    def test_list_show_correct_content(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 0)

    def test_list_with_object_show_correct_content(self):
        test_item = Item(
            name='test',
            is_published=True,
            category=self.category,
            text='Превосходно',
            is_on_main=True,
        )
        test_item.full_clean()
        test_item.save()

        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 1)

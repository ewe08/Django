from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Tag, Item


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        # Делаем запрос к главной странице и проверяем статус
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
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

    def test_homepage_show_correct_content(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 0)

    def test_homepage_with_objects_show_correct_content(self):
        test_item = Item(name='test',
                         is_published=True,
                         category=self.category,
                         text='Превосходно',
                         is_on_main=True,
                         )
        test_item.full_clean()
        test_item.save()

        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 1)

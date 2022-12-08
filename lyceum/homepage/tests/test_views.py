from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Item, Tag


class TaskPagesTests(TestCase):
    """Test item list on homepage response content"""

    def tearDown(self):
        Item.objects.all().delete()
        super().tearDown()

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category-slug',
            is_published=True,
            weight=50,
        )
        cls.tag = Tag.objects.create(
            name='Test tag',
            is_published=True,
            slug='test-tag-slug',
        )

    def test_homepage_show_correct_content(self):
        """Test show right item count and objects in context."""

        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 0)

    def test_homepage_with_objects_show_correct_content(self):
        """Test show correct objects content."""

        test_item = Item(
            name='test',
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

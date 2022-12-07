from django.test import Client, TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from catalog.models import Category, Tag, Item


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        # Делаем запрос к каталогу и проверяем статус
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(response.status_code, 200)


class RegularExpressionsTests(TestCase):
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

    # Правильные запросы
    def test_catalog_pk_true_endpoint(self):
        # Делаем запрос к каталогу по целому числу
        # И проверяем статусы
        test_item = Item(
            pk=123,
            name='test',
            is_published=True,
            category=self.category,
            text='Превосходно',
        )
        test_item.full_clean()
        test_item.save()
        response = Client().get(reverse('catalog:item_detail', args=[123]))
        self.assertEqual(response.status_code, 200)
        response = Client().get(reverse('catalog:item_detail', args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_catalog_pk_true_endpoint_2(self):
        test_item = Item(pk=1, name='test',
                         is_published=True,
                         category=self.category,
                         text='Превосходно',
                         )
        test_item.full_clean()
        test_item.save()
        response = Client().get(reverse('catalog:item_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    # Неправильные запросы
    def test_catalog_pk_false_endpoint(self):
        with self.assertRaises(NoReverseMatch):
            response = Client().get(reverse('catalog:item_detail', args=['abc']))

        with self.assertRaises(NoReverseMatch):
            # т.к. ноль - не положительное, ответ должен быть 404
            response = Client().get(reverse('catalog:item_detail', args=[0]))

        with self.assertRaises(NoReverseMatch):
            response = Client().get(reverse('catalog:item_detail', args=[-1]))

        with self.assertRaises(NoReverseMatch):
            response = Client().get(reverse('catalog:item_detail', args=['123abc']))

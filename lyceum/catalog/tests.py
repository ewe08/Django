from django.test import Client, TestCase
from django.core.exceptions import ValidationError

from .models import Category, Tag, Item


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        # Делаем запрос к каталогу и проверяем статус
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


class RegularExpressionsTests(TestCase):
    # Правильные запросы
    def test_catalog_pk_true_endpoint(self):
        # Делаем запрос к каталогу по целому числу
        # И проверяем статусы

        response = Client().get('/catalog/123/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)

    # Неправильные запросы
    def test_catalog_pk_false_endpoint(self):
        response = Client().get('/catalog/abc/')
        self.assertEqual(response.status_code, 404)

        # т.к. ноль - не положительное, ответ должен быть 404
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/123abc/')
        self.assertEqual(response.status_code, 404)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(name='Test Category',
                                               slug='test-category-slug',
                                               is_published=True, weight=50)
        cls.tag = Tag.objects.create(name='Test tag', is_published=True,
                                     slug='test-tag-slug')

    def test_has_no_words(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(name='Test item',
                             is_published=True,
                             category=self.category,
                             text='tut net prevoshodno')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count)

    def test_have_first_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test item #1',
                         is_published=True,
                         category=self.category,
                         text='tut est Превосходно')
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_have_second_word(self):
        item_count = Item.objects.count()
        self.item = Item(name='Test item#2',
                         is_published=True,
                         category=self.category,
                         text='tut est роскошно')
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_have_two_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test item#3',
                         is_published=True,
                         category=self.category,
                         text='tut est роскошно и превосходно')
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

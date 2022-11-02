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


class CategoryTest(TestCase):
    # Тест нулевого значения веса в категории
    def test_zero_weight(self):
        # Получение количества объектов до
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=0)
            test_category.full_clean()
            test_category.save()
        # Сраниванем с количеством после. Значения должны совпадать
        self.assertEqual(Category.objects.count(), category_count)

    # Тест отрицательного значения веса в категории
    def test_negative_weight(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=-14)
            test_category.full_clean()
            test_category.save()
        self.assertEqual(Category.objects.count(), category_count)

    # Тест граничного случая веса в категории
    def test_limit_weight(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=32767)
            test_category.full_clean()
            test_category.save()
        self.assertEqual(Category.objects.count(), category_count)

    # Тест веса значения намногов выше предела в категории
    def test_over_limit_weight(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=50000)
            test_category.full_clean()
            test_category.save()
        self.assertEqual(Category.objects.count(), category_count)

    # Тест правильного значения веса в категории
    def test_right_weight(self):
        category_count = Category.objects.count()
        test_category = Category(name='Test Category',
                                 slug='test-category-slug',
                                 is_published=True,
                                 weight=155)
        test_category.full_clean()
        test_category.save()
        # Количество объектов должно быть больше на 1, чем изначально
        self.assertEqual(Category.objects.count(), category_count + 1)


class ItemTest(TestCase):
    # Создание категорий и тэгов для теста
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(name='Test Category',
                                               slug='test-category-slug',
                                               is_published=True, weight=50)
        cls.tag = Tag.objects.create(name='Test tag', is_published=True,
                                     slug='test-tag-slug')

    # Тест предмета, если в описании нет обязательных слов
    # (превосходно или роскошно)
    def test_has_no_words(self):
        # Количество объектов до
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(name='Test item',
                             is_published=True,
                             category=self.category,
                             text='tut net prevoshodno')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
        # Количества объектов до и после должны быть равны
        self.assertEqual(Item.objects.count(), item_count)

    # Тест предмета, если в описании есть слово превосходно
    def test_have_first_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test item #1',
                         is_published=True,
                         category=self.category,
                         text='tut est Превосходно')
        self.item.full_clean()
        self.item.save()
        # Количества объектов до и после должны различаться на 1
        self.assertEqual(Item.objects.count(), item_count + 1)

    # Тест предмета, если в описании есть слово роскошно
    def test_have_second_word(self):
        item_count = Item.objects.count()
        self.item = Item(name='Test item#2',
                         is_published=True,
                         category=self.category,
                         text='tut est роскошно')
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    # Тест предмета, если в описании есть слова превосходно и роскошно
    def test_have_two_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test item#3',
                         is_published=True,
                         category=self.category,
                         text='tut est роскошно и превосходно')
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

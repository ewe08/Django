from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Category, Item, Tag


class CategoryTest(TestCase):
    """Test category model."""

    def tearDown(self):
        Category.objects.all().delete()
        super().tearDown()

    def test_zero_weight(self):
        """Test creating category with zero weight."""

        category_count = Category.objects.count()
        test_category = Category(name='Test Category',
                                 slug='test-category-slug',
                                 is_published=True,
                                 weight=0)
        test_category.full_clean()
        test_category.save()
        self.assertEqual(Category.objects.count(), category_count + 1)

    def test_negative_weight(self):
        """Test creating category with weight less than zero."""

        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=-14)
            test_category.full_clean()
            test_category.save()
        self.assertEqual(Category.objects.count(), category_count)

    def test_limit_weight(self):
        """Test creating category with weight equal to the limit."""

        category_count = Category.objects.count()
        test_category = Category(name='Test Category',
                                 slug='test-category-slug',
                                 is_published=True,
                                 weight=32767)
        test_category.full_clean()
        test_category.save()
        self.assertEqual(Category.objects.count(), category_count + 1)

    def test_over_limit_weight(self):
        """Test creating category with weight over limit."""

        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            test_category = Category(name='Test Category',
                                     slug='test-category-slug',
                                     is_published=True,
                                     weight=50000)
            test_category.full_clean()
            test_category.save()
        self.assertEqual(Category.objects.count(), category_count)

    def test_right_weight(self):
        """Test creating category with correct data."""

        category_count = Category.objects.count()
        test_category = Category(name='Test Category',
                                 slug='test-category-slug',
                                 is_published=True,
                                 weight=155)
        test_category.full_clean()
        test_category.save()
        self.assertEqual(Category.objects.count(), category_count + 1)


class ItemTest(TestCase):
    """Test item model."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category-slug',
            is_published=True, weight=50
        )
        cls.tag = Tag.objects.create(
            name='Test tag',
            is_published=True,
            slug='test-tag-slug'
        )

    def tearDown(self):
        Item.objects.all().delete()
        super().tearDown()

    def test_has_no_words(self):
        """Test creating item without required words in text."""

        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(
                name='Test item',
                is_published=True,
                category=self.category,
                text='tut net prevoshodno'
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count)

    def test_have_first_word(self):
        """Test creating item with first required word."""

        item_count = Item.objects.count()

        self.item = Item(
            name='Test item #1',
            is_published=True,
            category=self.category,
            text='tut est Превосходно'
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_have_second_word(self):
        """Test creating item with second required word."""

        item_count = Item.objects.count()
        self.item = Item(
            name='Test item#2',
            is_published=True,
            category=self.category,
            text='tut est роскошно'
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_have_two_word(self):
        """Test creating item with both required word."""

        item_count = Item.objects.count()

        self.item = Item(
            name='Test item#3',
            is_published=True,
            category=self.category,
            text='tut est роскошно и превосходно'
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_have_word_and_punct(self):
        """
        Test creating item with required word and punctuation mark after it.
        """

        item_count = Item.objects.count()

        self.item = Item(
            name='Test item#3',
            is_published=True,
            category=self.category,
            text='tut est роскошно!'
        )
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

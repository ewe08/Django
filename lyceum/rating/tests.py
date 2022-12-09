from catalog.models import Category, Item
from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase
from users.models import CustomUser

from .models import Rating


class RaitingModelTests(TestCase):
    """Test rating model."""

    def tearDown(self):
        Rating.objects.all().delete()
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
        cls.item = Item.objects.create(
            name='test',
            is_published=True,
            category=cls.category,
            text='Превосходно',
            is_on_main=True,
        )

    def test_create_rating(self):
        """Test create rating with correct params."""

        raiting_count = Rating.objects.count()
        custom_user = CustomUser(
            email=settings.TEST_USER_EMAIL,
            password='123',
        )
        custom_user.full_clean()
        custom_user.save()

        rating = Rating(
            user=custom_user,
            item=self.item,
            rate=1,
        )
        rating.full_clean()
        rating.save()
        self.assertEqual(Rating.objects.count(), raiting_count + 1)

    def test_once_rating(self):
        """Test create 2 ratings from one user to one item."""

        raiting_count = Rating.objects.count()
        custom_user = CustomUser(
            email=settings.TEST_USER_EMAIL,
            password='123',
        )
        custom_user.full_clean()
        custom_user.save()

        rating_1 = Rating(
            user=custom_user,
            item=self.item,
            rate=1
        )
        rating_1.full_clean()
        rating_1.save()
        with self.assertRaises(ValidationError):
            rating_2 = Rating(
                user=custom_user,
                item=self.item,
                rate=1
            )
            rating_2.full_clean()
            rating_2.save()
        self.assertEqual(Rating.objects.count(), raiting_count + 1)

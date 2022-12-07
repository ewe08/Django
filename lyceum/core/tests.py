import datetime as dt

from django.test import TestCase, Client
# from django.core.exceptions import ValidationError
from django.urls import reverse

from users.models import CustomUser


class BirthdayTests(TestCase):
    def tearDown(self):
        CustomUser.objects.all().delete()
        super().tearDown()

    def test_have_birthday(self):
        custom_user = CustomUser(
            email='test@test.com',
            password='123',
            birthday=dt.date.today(),
        )
        custom_user.full_clean()
        custom_user.save()

        response = Client().get(reverse('homepage:home'))

        self.assertIn(
            'birthday',
            response.context
        )

    def test_havent_birthday(self):
        custom_user = CustomUser(
            email='test@test.com',
            password='123',
            birthday=dt.date.today() + dt.timedelta(days=2),
        )
        custom_user.full_clean()
        custom_user.save()

        response = Client().get(reverse('homepage:home'))

        self.assertEqual(len(response.context['birthday']), 0)

    def test_many_birthdays(self):
        for i in range(1, 4):
            new_user = CustomUser(
                email=f'test{i}@test.com',
                password=f'1232048734{i}',
                birthday=dt.date.today(),
            )
            new_user.full_clean()
            new_user.save()
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(len(response.context['birthday']), 3)
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        # Делаем запрос к информационной странице и проверяем статус
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

from django.test import Client, TestCase


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

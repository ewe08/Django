from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    """Test homepage."""

    def test_homepage_endpoint(self):
        """Test response status by correct response."""

        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)

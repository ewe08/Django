from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    """Test about page."""

    def test_about_endpoint(self):
        """Test response status by correct response."""
        response = Client().get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)

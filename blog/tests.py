from django.test import TestCase
from django.urls import reverse


class BlogSmokeTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

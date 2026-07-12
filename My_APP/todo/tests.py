from django.test import TestCase
from django.urls import reverse

from .models import BlogPost


class PortfolioViewsTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Portfolio")

    def test_blog_creation(self):
        response = self.client.post(
            reverse("blog_create"),
            {"title": "My First Post", "content": "This is a test post."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(BlogPost.objects.filter(title="My First Post").exists())

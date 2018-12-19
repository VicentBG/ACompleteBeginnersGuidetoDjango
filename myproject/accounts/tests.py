from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .views import signup

# Create your tests here.

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

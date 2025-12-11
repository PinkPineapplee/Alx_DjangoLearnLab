from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_login_profile_flow(self):
        # Register
        resp = self.client.post(reverse('register'), {
            'username': 'tester',
            'email': 't@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        }, follow=True)
        self.assertTrue(resp.context['user'].is_authenticated)

        # Profile view accessible
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)

        # Logout
        resp = self.client.get(reverse('logout'), follow=True)
        self.assertFalse(resp.context['user'].is_authenticated)

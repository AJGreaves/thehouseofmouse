from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from accounts.views import register_view, profile_view

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile_view)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)
        
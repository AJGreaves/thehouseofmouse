from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import faqs_view, about_view, contact_view, privacy_view, terms_view

class TestUrls(SimpleTestCase):

    def test_faqs_url_is_resolved(self):
        url = reverse('faqs')
        self.assertEqual(resolve(url).func, faqs_view)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact_view)

    def test_privacy_url_is_resolved(self):
        url = reverse('privacy')
        self.assertEqual(resolve(url).func, privacy_view)

    def test_terms_url_is_resolved(self):
        url = reverse('terms')
        self.assertEqual(resolve(url).func, terms_view)
        

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from search.views import search_view

class TestUrls(SimpleTestCase):

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search_view)
        
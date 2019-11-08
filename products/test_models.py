from django.test import TestCase
from .models import Product


class ProductEntryTest(TestCase):
    """ Test Product model returns product title """
    def test_string_representation(self):
        product = Product(title="Test Mouse")
        self.assertEqual(str(product), product.title)

from django.test import TestCase
from cart.models import ShippingDestination, Order, OrderItem


class ShippingDestinationEntryTest(TestCase):
    """ Test ShippingDestination model returns country string """
    def test_string_representation(self):
        sd = ShippingDestination(country="Narnia")
        self.assertEqual(str(sd), sd.country)

    def test_default_shipping_time(self):
        sd = ShippingDestination(country="Narnia")
        self.assertEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_time(self):
        sd = ShippingDestination(country="Narnia", shipping_time="42")
        self.assertNotEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_price(self):
        sd = ShippingDestination(country="Narnia", shipping_price=42)
        self.assertEqual(sd.shipping_price, 42)
        self.assertNotEqual(sd.shipping_price, 99.99)


    # def test_get_absolute_url(self):
    #     pk = 99
    #     title = "Test Mouse"
    #     expected_result = '/products/listing/' + str(pk) + '/' + slugify(title)

    #     product = Product(pk=pk, title=title)
    #     result = Product.get_absolute_url(product)

    #     self.assertEqual(result, expected_result)
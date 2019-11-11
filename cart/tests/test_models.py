from django.test import TestCase
from cart.models import ShippingDestination, Order, OrderItem
from products.models import Product


class ShippingDestinationEntryTest(TestCase):
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

class OrderItemEntryTest(TestCase):

    def test_string_representation(self):
        product = Product(title="Test Mouse")
        order = Order(full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)
        expected_result = '3 x Test Mouse'
        self.assertEqual(str(order_item), expected_result)

from django.test import TestCase
from django.contrib.auth.models import User
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

    def test_order_id_on_order_item(self):
        product = Product(title="Test Mouse")
        order = Order(id=42, full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.order.id, 42)

    def test_product_id_in_order_item(self):
        product = Product(id=99, title="Test Mouse")
        order = Order(id=42, full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.product.id, 99)

class OrderEntryTest(TestCase):

    def test_string_representation(self):
        user = User(username="Trillian")
        order = Order(id=42, date_ordered='2019-11-10', customer=user)

        expected_result = '42-2019-11-10-Trillian'

        self.assertEqual(str(order), expected_result)

    def test_default_values(self):
        user = User(username="Trillian")
        order = Order(id=42, date_ordered='2019-11-10', customer=user)

        self.assertEqual(order.paid, False)
        self.assertEqual(order.shipped, False)

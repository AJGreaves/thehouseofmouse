from django.test import TestCase
from django.contrib.auth.models import User
from cart.models import ShippingDestination, Order, OrderItem
from products.models import Product


class ShippingDestinationEntryTest(TestCase):
    """ Tests for ShippingDestination model """

    def test_string_representation(self):
        """ Test that model returns correctly formatted string """

        sd = ShippingDestination(country="Narnia")
        self.assertEqual(str(sd), sd.country)

    def test_default_shipping_time(self):
        """ Test that default shipping time is added to model when no shippig time provided """

        sd = ShippingDestination(country="Narnia")
        self.assertEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_time(self):
        """ Test that default shipping time is no longer present when shipping time is provided """

        sd = ShippingDestination(country="Narnia", shipping_time="42 years")
        self.assertNotEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_price(self):
        """ Test that shipping price value is set correctly """

        sd = ShippingDestination(country="Narnia", shipping_price=42)
        self.assertEqual(sd.shipping_price, 42)
        self.assertNotEqual(sd.shipping_price, 99.99)

class OrderItemEntryTest(TestCase):

    def test_string_representation(self):
        """ Test that model returns correctly formatted string """

        product = Product(title="Test Mouse")
        order = Order(full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)

        expected_result = '3 x Test Mouse'
        
        self.assertEqual(str(order_item), expected_result)

    def test_order_id_on_order_item(self):
        """ Test that OrderItem model correctly stores the Id of is related Order instance """

        product = Product(title="Test Mouse")
        order = Order(id=42, full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.order.id, 42)

    def test_product_id_in_order_item(self):
        """ Test that OrderItem model correctly stores the id of its related Product instance """

        product = Product(id=99, title="Test Mouse")
        order = Order(id=42, full_name="Arthur Dent")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.product.id, 99)

class OrderEntryTest(TestCase):

    def test_string_representation(self):
        """ Test that model returns correctly formatted string """

        user = User(username="Trillian")
        order = Order(id=42, date_ordered='2019-11-10', customer=user)

        expected_result = '42-2019-11-10-Trillian'

        self.assertEqual(str(order), expected_result)

    def test_default_values(self):
        """ test that new Order instance sets it's paid and shipped boolean values to false """
        user = User(username="Trillian")
        order = Order(id=42, date_ordered='2019-11-10', customer=user)

        self.assertEqual(order.paid, False)
        self.assertEqual(order.shipped, False)

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import (
    cart_view,
    checkout_info_view,
    checkout_shipping_view,
    checkout_confirm_view
)

class TestUrls(SimpleTestCase):
    """ Tests for urls in cart app """

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func, cart_view)

    def test_checkout_info_url_is_resolved(self):
        url = reverse('info')
        self.assertEqual(resolve(url).func, checkout_info_view)

    def test_checkout_shipping_url_is_resolved(self):
        url = reverse('shipping')
        self.assertEqual(resolve(url).func, checkout_shipping_view)

    def test_checkout_confirm_url_is_resolved(self):
        url = reverse('confirm', args=['test-session-id'])
        self.assertEqual(resolve(url).func, checkout_confirm_view)
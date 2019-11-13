from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Order, ShippingDestination

class TestCartViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):
        """ checks that user not logged in is redirected to login page """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/")


class TestCartViewLoggedIn(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )
    
    def test_response_status_200(self):
        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_load_page_with_no_cart_contents(self):
        client = Client()

        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        context = response.context
        self.assertTrue(context['nothing_in_cart'])


class TestCheckoutInfoViewLoggedPut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):
        """ checks that user not logged in is redirected to login page """
        response = self.client.get('/cart/checkout/info/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/checkout/info/")

class TestCheckoutInfoViewLoggedIn(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )
    
    def test_user_logged_in_but_nothing_in_cart_redirect(self):
        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/checkout/info/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/cart/")


    def test_post_new_order_form_correct(self):
        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product in database
        product = Product()
        product.id = 3
        product.price = 20
        product.num_in_stock = 10
        product.description = "description"
        product.tags = "tags"
        product.save()
        
        country = ShippingDestination.objects.create(country="UK", shipping_price=10)
        Order.objects.create(customer=self.user)

        # create session data for product
        session = client.session
        session['cart'] = {'orderItems': [{'listingId': 3, 'quantity': 1}], 'total': 20, 'count': 1}
        session.save()

        client.post(
            '/cart/checkout/info/',
            {
                'full_name': 'Arthur Dent',
                'address_line_1': 'Street House 1',
                'town_or_city': 'City',
                'county': 'Devon',
                'postcode': '1234CB',
                'country': country.id,
            }
        )

        order = Order.objects.filter(customer=self.user).first()
        self.assertEqual(order.full_name, "Arthur Dent")
        self.assertEqual(order.county, "Devon")
        self.assertEqual(order.country, country)
        self.assertIsInstance(order, Order)

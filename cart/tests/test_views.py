from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Order, ShippingDestination

class TestCartViewLoggedOut(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):
        """ checks that user not logged in is redirected to login page """

        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/")


class TestCartViewLoggedIn(TestCase):
    """ Tests for cart view when user is logged in """

    def setUp(self):
        """ Creates instance of user in test database so login status can be achieved """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )
    
    def test_response_status_200(self):
        """ Test that Logged in user is not redirected from cart page """

        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_load_page_with_no_cart_contents(self):
        """ Test that view context includes nothing_in_cart set to true when page loaded with no cart items in session """

        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        context = response.context
        self.assertTrue(context['nothing_in_cart'])


class TestCheckoutInfoViewLoggedPut(TestCase):
    """ Test for checkout info view when user is logged out """

    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):
        """ checks that user not logged in is redirected to login page """

        response = self.client.get('/cart/checkout/info/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/checkout/info/")

class TestCheckoutInfoViewLoggedIn(TestCase):
    """ Test for checkout info view when user is logged out """

    def setUp(self):
        """ Creates instance of user in test database so login status can be achieved """

        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )
    
    def test_user_logged_in_but_nothing_in_cart_redirect(self):
        """
        Tests that view redirects to cart page when logged in user tries to 
        access this page but does not have anything in their cart
        """

        # logs user in
        client = Client()
        client.login(username='testuser', password="testing321")

        # gets response
        response = client.get('/cart/checkout/info/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/cart/")


    def test_post_new_order_form_correct(self):
        """ Test that post request to checkout info view is received and processed into the database correctly """

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

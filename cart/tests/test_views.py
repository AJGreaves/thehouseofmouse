from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from products.models import Product
from cart.forms import NewOrderForm
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

    def test_load_page_with_cart_contents(self):
        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product in database
        Product.objects.create(
            id=3,
            title="Test Mouse",
            price=20,
            num_in_stock=10,
            description="description",
            tags="tags",
            product_image1="test.jpg",
        )

        # create session data for product
        session = client.session
        session['cart'] = {'orderItems': [{'listingId': 3, 'quantity': 1}], 'total': 20, 'count': 1}
        session.save()

        # get response and context
        response = client.get('/cart/')
        context = response.context
        cart = context['cart_items']

        self.assertIn("Test Mouse", str(cart))


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

    def test_info_form_in_context(self):
        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product in database
        Product.objects.create(
            id=3,
            title="Test Mouse",
            price=20,
            num_in_stock=10,
            description="description",
            tags="tags",
            product_image1="test.jpg",
        )
        Order.objects.create(customer=self.user)

        # create session data for product
        session = client.session
        session['cart'] = {'orderItems': [{'listingId': 3, 'quantity': 1}], 'total': 20, 'count': 1}
        session.save()

        # get response and context
        response = client.get('/cart/checkout/info/')
        form = response.context['form']
        form_type = type(form)
        self.assertEqual(form_type, NewOrderForm)

    def test_load_initial_data_in_form(self):
        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product, country and order in database
        Product.objects.create(
            id=3,
            title="Test Mouse",
            price=20,
            num_in_stock=10,
            description="description",
            tags="tags",
            product_image1="test.jpg",
        )
        country = ShippingDestination.objects.create(country="UK", shipping_price=10)
        Order.objects.create(
            customer=self.user,
            full_name="Arthur Dent",
            address_line_1="155 Country Lane",
            town_or_city="Cottington",
            county="Cottingshire",
            country=country,
        )

        # create session data for product
        session = client.session
        session['cart'] = {'orderItems': [{'listingId': 3, 'quantity': 1}], 'total': 20, 'count': 1}
        session.save()

        # get response and context
        response = client.get('/cart/checkout/info/')
        form = response.context['form']

        self.assertIn("Arthur Dent", str(form))
        self.assertIn("155 Country Lane", str(form))
        self.assertIn("Cottingshire", str(form))
        self.assertIn("UK", str(form))

    def test_post_new_order_form_correct(self):
        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product in database
        Product.objects.create(
            id=3,
            title="Test Mouse",
            price=20,
            num_in_stock=10,
            description="description",
            tags="tags",
            product_image1="test.jpg",
        )
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

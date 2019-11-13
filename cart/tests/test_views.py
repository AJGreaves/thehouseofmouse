from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from products.models import Product

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

from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from accounts.forms import UserUpdateForm, UserRegisterForm
from cart.models import Order, OrderItem, ShippingDestination
from products.models import Product
from accounts.views import register_view, profile_view

class TestRegisterViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/accounts/register/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('register.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

    def test_register_form_in_context(self):
        response = self.client.get('/accounts/register/')
        form = response.context['form']
        form_type = type(form)
        self.assertEqual(form_type, UserRegisterForm)

class TestRegisterViewLoggedIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )
    
    def test_register_page_redirect_to_home_if_logged_in(self):
        request = self.factory.get('/')
        request.user = self.user
        response = register_view(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

class TestProfileViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_profile_view_not_logged_in(self):
        response = self.client.get('/accounts/profile/')
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/profile/')

class TestProfileViewLoggedIn(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )

    def test_profile_view_logged_in(self):
        request = self.factory.get('/')
        request.user = self.user
        response = profile_view(request)
        
        self.assertEqual(response.status_code, 200)

    def test_users_orders_in_context(self):
        client = Client()
        client.login(username='testuser', password="testing321")

        country = ShippingDestination.objects.create(country="UK", shipping_price=10)
        order = Order.objects.create(customer=self.user, country=country, paid=True)
        product = Product.objects.create(
            title="Test Mouse",
            price=42,
            num_in_stock=10,
            description="description",
            tags="tags"
        )
        order_item = OrderItem.objects.create(order=order, product=product, quantity=1)

        response = client.get('/accounts/profile/')
        all_orders = response.context['all_orders']

        self.assertIn(str(order.customer), str(all_orders))
        self.assertIn(str(order_item.product), str(all_orders))
        
    def test_user_form_in_context(self):
        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/accounts/profile/')
        form = response.context['form']
        form_type = type(form)
        self.assertEqual(form_type, UserUpdateForm)

    def test_loaded_templates(self):
        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/accounts/profile/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('profile.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names
from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from accounts.views import register_view

class TestRegisterViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/accounts/register/')
        templates = response.templates

        names = []
        for t in templates:
            names.append(t.name)

        self.assertIn('base.html', str(names))
        self.assertIn('register.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

    def test_register_form_fields(self):
        response = self.client.get('/accounts/register/')
        form = response.context['form']
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

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

        
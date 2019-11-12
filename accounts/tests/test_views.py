from unittest import TestCase
from django.test import Client

class TestRegisterView(TestCase):
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

    # def test_register_page_redirect_if_logged_in(self):
    #     c = Client()
    #     c.login(username='TestUser', password='testing321')
    #     response = c.get('/accounts/register/', follow=True)
    #     self.assertEqual(response.redirect_chain, [('/', 302)])

    # c = Client()
    # response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    # response.status_code
from django.test import Client, TestCase
from pages.forms import ContactForm

class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('index.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

class TestFaqsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/faqs/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/faqs/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('faqs.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

class TestAboutView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/about/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('about.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

class TestContactView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/contact/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/contact/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('contact.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

    def test_contact_form_in_context(self):
        response = self.client.get('/pages/contact/')
        form = response.context['form']

        self.assertEqual(type(form), ContactForm)

class TestPrivacyView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/privacy/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/privacy/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('privacy.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

class TestTermsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/terms-and-conditions/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/terms-and-conditions/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('terms.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names
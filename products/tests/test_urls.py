from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    AllProductsView,
    AllProductsPriceHighView,
    AllProductsPriceLowView,
    ListingDetailView,
    famous_category_view,
    special_category_view,
    harry_potter_category_view,
    starwars_category_view,
    misc_category_view,
    jobs_category_view,
    doctor_who_category_view,
    xmas_category_view,
    halloween_category_view,
    categories_view
)

class TestUrls(SimpleTestCase):

    def test_listing_detail_url_is_resolved(self):
        url = reverse('listing-detail', args=[5, 'test-title'])
        self.assertEqual(resolve(url).func.view_class, ListingDetailView)
    
    def test_categories_url_is_resolved(self):
        url = reverse('categories')
        self.assertEqual(resolve(url).func, categories_view)

    def test_all_products_url_is_resolved(self):
        url = reverse('all-products')
        self.assertEqual(resolve(url).func.view_class, AllProductsView)

    def test_all_products_price_high_url_is_resolved(self):
        url = reverse('all-products-price-high')
        self.assertEqual(resolve(url).func.view_class, AllProductsPriceHighView)

    def test_all_products_price_low_url_is_resolved(self):
        url = reverse('all-products-price-low')
        self.assertEqual(resolve(url).func.view_class, AllProductsPriceLowView)

    def test_famous_url_is_resolved(self):
        url = reverse('famous')
        self.assertEqual(resolve(url).func, famous_category_view)

    def test_special_occasions_url_is_resolved(self):
        url = reverse('special-occasions')
        self.assertEqual(resolve(url).func, special_category_view)

    def test_harry_potter_url_is_resolved(self):
        url = reverse('harry-potter')
        self.assertEqual(resolve(url).func, harry_potter_category_view)

    def test_star_wars_url_is_resolved(self):
        url = reverse('star-wars')
        self.assertEqual(resolve(url).func, starwars_category_view)

    def test_weird_url_is_resolved(self):
        url = reverse('weird-misc')
        self.assertEqual(resolve(url).func, misc_category_view)

    def test_jobs_url_is_resolved(self):
        url = reverse('jobs-hobbies')
        self.assertEqual(resolve(url).func, jobs_category_view)

    def test_doctor_who_url_is_resolved(self):
        url = reverse('doctor-who')
        self.assertEqual(resolve(url).func, doctor_who_category_view)

    def test_xmas_url_is_resolved(self):
        url = reverse('christmas')
        self.assertEqual(resolve(url).func, xmas_category_view)

    def test_halloween_url_is_resolved(self):
        url = reverse('halloween')
        self.assertEqual(resolve(url).func, halloween_category_view)

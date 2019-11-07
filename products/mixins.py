from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Product

class ProductMixin(ListView):
    model = Product
    template_name = 'results.html'
    context_object_name = 'products'
    paginate_by = 12

class AllProductsMixin(ListView):
    queryset = Product.objects.all()

class SortAllMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'all-products'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class FamousProductsMixin(ListView):
    queryset = Product.objects.filter(category="Famous")

class SortFamousMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'famous'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SpecialProductsMixin(ListView):
    queryset = Product.objects.filter(category="Special Occasions")

class SortSpecialMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'special-occasions'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortHarryMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'harry-potter'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortStarWarsMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'star-wars'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortWeirdMiscMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'weird-misc'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortJobsMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'jobs-hobbies'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortDrWhoMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'doctor-who'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortXmasMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'christmas'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))

class SortHalloweenMixin(ListView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_category = 'halloween'
            sort = request.POST.get('results-sort-select')
            if sort == 'price-high':
                return redirect(reverse(f'{product_category}-price-high'))
            elif sort == 'price-low':
                return redirect(reverse(f'{product_category}-price-low'))
            elif sort == 'featured':
                return redirect(reverse(product_category))
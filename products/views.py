import json
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
from .models import Product
from .mixins import (
    ProductMixin,
    AllProductsMixin,
    SortAllMixin,
    SortFamousMixin,
    FamousProductsMixin,
    SortSpecialMixin,
    SpecialProductsMixin,
    SortHarryMixin,
    HarryProductsMixin,
    SortStarWarsMixin,
    SortWeirdMiscMixin,
    SortJobsMixin,
    SortDrWhoMixin,
    SortXmasMixin,
    SortHalloweenMixin
)

# Create your views here.
class ListingDetailView(DetailView):
    """ Create view for individual listings """
    model = Product
    template_name = 'listing.html'
    context_object_name = 'product'
    extra_context = {}

    def get_object(self, queryset=Product):
        _id = self.kwargs.get('pk')
        instance = get_object_or_404(Product, id=_id)

        self.extra_context['product'] = instance
        self.extra_context['stock_arr'] = [x for x in range(instance.num_in_stock)]
        self.extra_context['more_products'] = Product.objects.all().filter(category=instance.category).exclude(id=_id).order_by('-featured')[:6]

        return instance

    def post(self, request, *args, **kwargs):
        """ Processes fetch request and adds shopping cart data to session storage """
        form = json.loads(request.body)
        _id = self.kwargs.get('pk')
        instance = get_object_or_404(Product, id=_id)

        # checks if orderItems already exists in session storage, and creates it if needed.
        cart = request.session.get('cart', {'orderItems': [], 'total': 0, 'count': 0})
        
        item_already_in_cart = False
        too_many = False

        # if cart already exists, check if selected item is already in cart orderItems
        if len(cart['orderItems']) != 0:
            for item in cart['orderItems']:
                listingId = item.get("listingId")

                # if listing is already in cart set to true, check num in stock against num requested by user
                if listingId == _id:
                    item_already_in_cart = True
                    num_in_stock = instance.num_in_stock
                    quantity_total = int(item['quantity']) + int(form['quantity'])

                    # if quantity requested is more than is in stock set quantity
                    # of item to number in stock and send response to js to alert user
                    if quantity_total > num_in_stock:
                        diff = quantity_total - num_in_stock
                        item['quantity'] = int(num_in_stock)
                        too_many = True
                    else:
                        item['quantity'] = int(quantity_total)

            # if item not already in cart, append new item to orderItems
            if not item_already_in_cart:
                cart['orderItems'].append({'listingId': _id, 'quantity': int(form['quantity'])})
        
        # if brand new cart, add first orderItem to it
        else:
            cart['orderItems'].append({'listingId': _id, 'quantity': int(form['quantity'])})

        # set values for count and total for new item in cart
        if not too_many:
            cart['count'] = cart['count'] + int(form['quantity'])
            cart['total'] = round(cart['total'] + float(Decimal(instance.price) * Decimal(form['quantity'])))
        
        # set values for count and total based on the number of items
        # in stock rather than number of items user requested
        else:
            quantity_to_add = int(form['quantity']) - diff
            cart['count'] = cart['count'] + quantity_to_add
            cart['total'] = round(cart['total'] + float(Decimal(instance.price) * quantity_to_add))

            
        request.session['cart'] = cart
        print(cart)
        data = {
            'title': instance.title,
            'quantity': form['quantity'],
            'too_many': too_many
        }
        return JsonResponse(data)

def categories_view(request, *args, **kwargs):
    """
    Display all categories for users to choose from.
    """
    return render(request, "categories.html")

def results_view(request, *args, **kwargs):
    """ results_view can be used for search results, category or favourites """
    return render(request, "results.html")

# All products

    model = Product
    template_name = 'results.html'
    ordering = ['-featured']
    context_object_name = 'products'
    paginate_by = 10

    ordering = ['-featured']
    
    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
        context['category'] = 'All Products'
        context['select'] = 'featured'
        return context

class AllProductsPriceHighView(ProductMixin, AllProductsMixin, SortAllMixin):

    ordering = ['-price']

    def get_context_data(self, **kwargs):
        context = super(AllProductsPriceHighView, self).get_context_data(**kwargs)
        context['category'] = 'All Products'
        context['select'] = 'price-high'
        return context

class AllProductsPriceLowView(ProductMixin, AllProductsMixin, SortAllMixin):

    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super(AllProductsPriceLowView, self).get_context_data(**kwargs)
        context['category'] = 'All Products'
        context['select'] = 'price-low'
        return context

# Famous category

class FamousView(ProductMixin, FamousProductsMixin, SortFamousMixin):

    ordering = ['-featured']

    def get_context_data(self, **kwargs):
        context = super(FamousView, self).get_context_data(**kwargs)
        context['category'] = 'Famous'
        context['select'] = 'featured'
        return context

class FamousPriceHighView(ProductMixin, FamousProductsMixin, SortFamousMixin):

    ordering = ['-price']

    def get_context_data(self, **kwargs):
        context = super(FamousPriceHighView, self).get_context_data(**kwargs)
        context['category'] = 'Famous'
        context['select'] = 'price-high'
        return context

class FamousPriceLowView(ProductMixin, FamousProductsMixin, SortFamousMixin):

    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super(FamousPriceLowView, self).get_context_data(**kwargs)
        context['category'] = 'Famous'
        context['select'] = 'price-low'
        return context

# Special Occasions category

class SpecialView(ProductMixin, SpecialProductsMixin, SortSpecialMixin):

    ordering = ['-featured']

    def get_context_data(self, **kwargs):
        context = super(SpecialView, self).get_context_data(**kwargs)
        context['category'] = 'Special Occasions'
        return context

class SpecialPriceHighView(ProductMixin, SpecialProductsMixin, SortSpecialMixin):

    ordering = ['-price']

    def get_context_data(self, **kwargs):
        context = super(SpecialPriceHighView, self).get_context_data(**kwargs)
        context['category'] = 'Special Occasions'
        return context

class SpecialPriceLowView(ProductMixin, SpecialProductsMixin, SortSpecialMixin):

    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super(SpecialPriceLowView, self).get_context_data(**kwargs)
        context['category'] = 'Special Occasions'
        return context

# Harry Potter category

class HarryView(ProductMixin, HarryProductsMixin, SortHarryMixin):

    ordering = ['-featured']

    def get_context_data(self, **kwargs):
        context = super(HarryView, self).get_context_data(**kwargs)
        context['category'] = 'Harry Potter'
        return context

class HarryPriceHighView(ProductMixin, HarryProductsMixin, SortHarryMixin):

    ordering = ['-price']

    def get_context_data(self, **kwargs):
        context = super(HarryPriceHighView, self).get_context_data(**kwargs)
        context['category'] = 'Harry Potter'
        return context

class HarryPriceLowView(ProductMixin, HarryProductsMixin, SortHarryMixin):

    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super(HarryPriceLowView, self).get_context_data(**kwargs)
        context['category'] = 'Harry Potter'
        return context


def harry_potter_category_view(request, *args, **kwargs):
    """
    Render all listings in "Harry Potter" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Harry Potter')
        return render(request, "results.html", context)

    context = get_context('Harry Potter')
    return render(request, "results.html", context)


def starwars_category_view(request, *args, **kwargs):
    """
    Render all listings in "Star Wars" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Star Wars')
        return render(request, "results.html", context)

    context = get_context('Star Wars')
    return render(request, "results.html", context)


def misc_category_view(request, *args, **kwargs):
    """
    Render all listings in "Weird & Misc" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Weird & Misc')
        return render(request, "results.html", context)

    context = get_context('Weird & Misc')
    return render(request, "results.html", context)


def jobs_category_view(request, *args, **kwargs):
    """
    Render all listings in "Jobs & Hobbies" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Jobs & Hobbies')
        return render(request, "results.html", context)

    context = get_context('Jobs & Hobbies')
    return render(request, "results.html", context)


def doctor_who_category_view(request, *args, **kwargs):
    """
    Render all listings in "Doctor Who" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Doctor Who')
        return render(request, "results.html", context)

    context = get_context('Doctor Who')
    return render(request, "results.html", context)


def xmas_category_view(request, *args, **kwargs):
    """
    Render all listings in "Christmas" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Christmas')
        return render(request, "results.html", context)

    context = get_context('Christmas')
    return render(request, "results.html", context)


def halloween_category_view(request, *args, **kwargs):
    """
    Render all listings in "Halloween" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Halloween')
        return render(request, "results.html", context)

    context = get_context('Halloween')
    return render(request, "results.html", context)


def get_post_request_context(post_request, category_name):
    """
    Takes request and the relevant category name, and pulls the 
    necessary context to fit the filer the user selected.
    """
    sort = post_request.POST.get('results-sort-select')
    if sort == 'price-high':
        results = Product.objects.all().filter(category=category_name).order_by('-price')
    elif sort == 'price-low':
        results = Product.objects.all().filter(category=category_name).order_by('price')
    elif sort == 'featured':
        results = Product.objects.all().filter(category=category_name).order_by('-featured')
    context = {
        'products': results,
        'select': sort,
        'category': category_name
    }
    return context

def get_context(category_name):
    context = {
        'products': Product.objects.all().filter(category=category_name).order_by('-featured'),
        'category': category_name
    }
    return context
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

# Create your views here.
class ListingDetailView(DetailView):

    """ Create view for individual listings """
    model = Product
    template_name = 'listing.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """
        Get the current context and the relevant pk, then set the
        context needed for building the select dropdown menu.
        """
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']

        product = Product.objects.get(id=pk)
        num_in_stock = product.num_in_stock

        stock_arr = []
        for i in range(num_in_stock):
            stock_arr.append(i)

        # retrieve products from the same category (excluding the current listing)
        # to display in "more like this" section of the page.
        more_products = Product.objects.all().filter(category=product.category).exclude(id=pk).order_by('-featured')[:6]

        context['product'] = product
        context['stock_arr'] = stock_arr
        context['more_products'] = more_products

        return context


def results_view(request, *args, **kwargs):
    """ results_view can be used for search results, category or favourites """
    return render(request, "results.html")


def all_products_view(request, *args, **kwargs):
    """
    Displays all products. If user selects an option to sort listings
    by featured or price, loads content in order requested.
    """
    if request.method == 'POST':
        sort = request.POST.get('results-sort-select')
        if sort == 'price-high':
            results = Product.objects.all().order_by('-price')
        elif sort == 'price-low':
            results = Product.objects.all().order_by('price')
        elif sort == 'featured':
            results = Product.objects.all().order_by('-featured')
        context = {
            'products': results,
            'select': sort,
            'category': 'All Products'
        }
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().order_by('-featured'),
        'category': 'All Products',
    }
    return render(request, "results.html", context)

def categories_view(request, *args, **kwargs):
    """
    Display all categories for users to choose from.
    """
    return render(request, "categories.html")

def famous_category_view(request, *args, **kwargs):
    """
    Render all listings in "famous" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Famous')
        return render(request, "results.html", context)

    context = get_context('Famous')
    return render(request, "results.html", context)


def special_category_view(request, *args, **kwargs):
    """
    Render all listings in "Special Occasions" category.
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Special Occasions')
        return render(request, "results.html", context)

    context = get_context('Special Occasions')
    return render(request, "results.html", context)


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
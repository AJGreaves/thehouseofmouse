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

        context['product'] = product
        context['stock_arr'] = stock_arr

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
        return render(request, "all_products.html", context)

    context = {
        'products': Product.objects.all().order_by('-featured'),
        'category': 'All Products',
    }
    return render(request, "results.html", context)


def famous_category_view(request, *args, **kwargs):
    """
    Render all listings in "famous" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Famous')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Famous"),
        'category': 'Famous'
    }
    return render(request, "results.html", context)

def special_category_view(request, *args, **kwargs):
    """
    Render all listings in "Special Occasions" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Special Occasions')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Special Occasions"),
        'category': 'Special Occasions'
    }
    return render(request, "results.html", context)

def harry_potter_category_view(request, *args, **kwargs):
    """
    Render all listings in "Harry Potter" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Harry Potter')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Harry Potter"),
        'category': 'Harry Potter'
    }
    return render(request, "results.html", context)

def starwars_category_view(request, *args, **kwargs):
    """
    Render all listings in "Star Wars" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Star Wars')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Star Wars"),
        'category': 'Star Wars'
    }
    return render(request, "results.html", context)

def misc_category_view(request, *args, **kwargs):
    """
    Render all listings in "Weird & Misc" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Weird & Misc')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Weird & Misc"),
        'category': 'Weird & Misc'
    }
    return render(request, "results.html", context)

def jobs_category_view(request, *args, **kwargs):
    """
    Render all listings in "Jobs & Hobbies" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Jobs & Hobbies')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Jobs & Hobbies"),
        'category': 'Jobs & Hobbies'
    }
    return render(request, "results.html", context)

def doctor_who_category_view(request, *args, **kwargs):
    """
    Render all listings in "Doctor Who" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Doctor Who')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Doctor Who"),
        'category': 'Doctor Who'
    }
    return render(request, "results.html", context)

def xmas_category_view(request, *args, **kwargs):
    """
    Render all listings in "Christmas" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Christmas')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Christmas"),
        'category': 'Christmas'
    }
    return render(request, "results.html", context)

def halloween_category_view(request, *args, **kwargs):
    """
    Render all listings in "Halloween" category.
    """

    if request.method == 'POST':
        context = render_category_page(request, 'Halloween')
        return render(request, "results.html", context)

    context = {
        'products': Product.objects.all().filter(category="Halloween"),
        'category': 'Halloween'
    }
    return render(request, "results.html", context)

def render_category_page(post_request, category_name):
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
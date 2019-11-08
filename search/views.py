from django.shortcuts import render, reverse, redirect
from products.models import Product
from django.db.models import Q #for multiple searches

# Create your views here.

def search_view(request, *args, **kwargs):

    products = Product.objects.all().order_by('-featured')
    context = {
        'products': products,
        'category': 'Search'
    }

    if request.method == 'POST':
        query = request.POST.get('query')

        return redirect(reverse('search-results', kwargs={'query': query}))

    return render(request, "results.html", context)


def search_results_view(request, *args, **kwargs):

    if request.method == 'POST':
        query = request.POST.get('query')
        context = do_search(query)
        return render(request, "results.html", context)
    else:
        query = kwargs.get('query')
        context = do_search(query)
        return render(request, "results.html", context)


def do_search(query):
    results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
    context = {
        'products': results,
        'category': 'Search',
        'search_params': query
    }

    return context
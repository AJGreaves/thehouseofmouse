from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator
from itertools import chain
from products.models import Product

# Create your views here.

def search_view(request, *args, **kwargs):
    """
    View for search page. Before search query is entered, displays all products in database ordered by featured items first.
    If search query entered view takes query and filters results from Product model input and provides the list for
    display on the page.
    """
    featured = Product.objects.filter(featured=True)
    not_featured = Product.objects.filter(featured=False)
    products_list = list(chain(featured, not_featured))
    paginator = Paginator(products_list, 12)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'category': 'Search',
        'page': 'search',
    }

    query = request.GET.get('query')
    if query:
        vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('tags', weight='C')
        query = SearchQuery(query)
        results = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('rank')
        paginator = Paginator(results, 12)

        page = request.GET.get('page')
        products = paginator.get_page(page)

        context = {
            'products': products,
            'category': 'Search',
            'page': 'search',
            'search_params': query
        }

        return render(request, "results.html", context)

    return render(request, "results.html", context)



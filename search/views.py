from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator
from products.models import Product

# Create your views here.

def search_view(request, *args, **kwargs):
    """
    View for search page. If search query entered view takes query and filters results from Product model input and provides the list for
    display on the page.
    """

    context = {
        'category': 'Search',
        'page': 'search',
        'no_search_yet': True
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



from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from products.models import Product

# Create your views here.
def search_view(request, q='', *args, **kwargs):
    results = Product.objects.annotate(
        search=SearchVector('title', 'description', 'tags')
    ).filter(search=q)

    context = {
        'products': results,
        'category': 'search',
        'search_params': q
    }

    return render(request, "results.html", context)
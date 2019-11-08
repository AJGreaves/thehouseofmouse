from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product
from django.db.models import Q #for multiple searches

# Create your views here.

def search_view(request, *args, **kwargs):
    """
    View for search page. If search query entered view takes query
    and filters results from Product model input
    """
    products_list = Product.objects.all().order_by('-featured')
    paginator = Paginator(products_list, 12)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'category': 'Search',
        'page': 'search',
    }

    if request.method == 'POST':
        query = request.POST.get('query')
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))

        context = {
            'products': results,
            'category': 'Search',
            'page': 'search',
            'search_params': query
        }

        return render(request, "results.html", context)

    return render(request, "results.html", context)



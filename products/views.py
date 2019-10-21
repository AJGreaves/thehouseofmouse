from django.shortcuts import render
from .models import Product

# Create your views here.
def listing_view(request, *args, **kwargs):
    product = Product.objects.get(id=1)
    context = {
        'title': product.title,
        'description': product.description,
        'price': product.price,
        'category': product.category,
        'num_in_stock': product.num_in_stock,
    }
    return render(request, "listing.html", context)

def results_view(request, *args, **kwargs):
    """ results_view can be used for search results, category or favourites """
    return render(request, "results.html")
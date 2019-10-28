from django.shortcuts import render
from products.models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    featured_products = Product.objects.order_by('-featured', '?')[:6]
    context = {
        'featured_products': featured_products,
        'category': 'All Products',
        'page': 'home',
    }
    return render(request, "index.html", context)

def faqs_view(request, *args, **kwargs):
    return render(request, "faqs.html", {"page": "faqs"})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {"page": "about"})
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
        }
        return render(request, "all_products.html", context)

    context = {
        'products': Product.objects.all().order_by('-featured')
    }
    return render(request, "all_products.html", context)
from django.shortcuts import render

# Create your views here.
def listing_view(request, *args, **kwargs):
    return render(request, "listing.html")

def results_view(request, *args, **kwargs):
    """ results_view can be used for search results, category or favourites """
    return render(request, "results.html")
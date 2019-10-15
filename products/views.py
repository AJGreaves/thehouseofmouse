from django.shortcuts import render

# Create your views here.
def listing_view(request, *args, **kwargs):
    return render(request, "listing.html")
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        "page": "home"
    }
    return render(request, "pages/index.html", context)

def listing_view(request, *args, **kwargs):
    return render(request, "pages/listing.html")

def faqs_view(request, *args, **kwargs):
    return render(request, "pages/faqs.html")

def about_view(request, *args, **kwargs):
    return render(request, "pages/about.html")
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/index.html", {"page": "home"})

def faqs_view(request, *args, **kwargs):
    return render(request, "pages/faqs.html", {"page": "faqs"})

def about_view(request, *args, **kwargs):
    return render(request, "pages/about.html", {"page": "about"})
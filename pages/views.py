from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        "page": "home"
    }
    return render(request, "pages/index.html", context)

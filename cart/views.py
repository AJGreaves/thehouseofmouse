from django.shortcuts import render

# Create your views here.
def cart_view(request, *args, **kwargs):
    return render(request, "cart.html")
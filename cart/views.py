from django.shortcuts import render

# Create your views here.
def cart_view(request, *args, **kwargs):
    """ 
    render shopping cart page, remove footer from this page 
    to fit conventions of other eCommerce sites 
    """
    return render(request, "cart.html", {"footer": False})

def checkout1_view(request, *args, **kwargs):
    return render(request, "checkout1.html")

def checkout2_view(request, *args, **kwargs):
    return render(request, "checkout2.html")

def checkout3_view(request, *args, **kwargs):
    return render(request, "checkout3.html")

def checkout4_view(request, *args, **kwargs):
    return render(request, "checkout4.html")
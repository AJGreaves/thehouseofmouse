from django.shortcuts import render

# Context objects

"""
Removes navbar and footer for checkout process, as
is convention for online stores to guide buyers to final purchase
"""
nav_and_footer = {
    "footer": False,
    "navbar": False
}


# Create your views here.
def cart_view(request, *args, **kwargs):
    """ 
    render shopping cart page, remove footer from this page 
    to fit conventions of other eCommerce sites 
    """
    return render(request, "cart.html", {"footer": False})

def checkout1_view(request, *args, **kwargs):

    return render(request, "checkout1.html", nav_and_footer)

def checkout2_view(request, *args, **kwargs):
    return render(request, "checkout2.html", nav_and_footer)

def checkout3_view(request, *args, **kwargs):
    return render(request, "checkout3.html", nav_and_footer)

def checkout4_view(request, *args, **kwargs):
    return render(request, "checkout4.html", nav_and_footer)
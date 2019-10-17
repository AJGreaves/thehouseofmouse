from django.shortcuts import render

# Context objects


# Create your views here.
def cart_view(request, *args, **kwargs):
    """ 
    render shopping cart page, remove footer from this page 
    to fit conventions of other eCommerce sites 
    """
    return render(request, "cart.html", {"footer": False})

def checkout_info_view(request, *args, **kwargs):
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_info"
    }
    return render(request, "checkout1.html", context)

def checkout_shipping_view(request, *args, **kwargs):
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_shipping"
    }
    return render(request, "checkout2.html", context)

def checkout_payment_view(request, *args, **kwargs):
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_payment"
    }
    return render(request, "checkout3.html", context)

def checkout_confirm_view(request, *args, **kwargs):
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_confirm"
    }
    return render(request, "checkout4.html", context)
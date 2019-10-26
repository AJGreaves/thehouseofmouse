from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product

# Create your views here.
@login_required
def cart_view(request, *args, **kwargs):
    """
    render shopping cart page, remove footer from this page
    to fit conventions of other eCommerce sites
    """
    cart = request.session.get('cart')

    cart_products = []

    for item in cart['orderItems']:
        _id = item['listingId']
        product = Product.objects.filter(id=_id).first()
        cart_products.append({'product': product, 'quantity': item['quantity']})
    print(cart)
    print(cart_products)

    context = {
        'products' : cart_products,
        "footer": False
    }

    return render(request, "cart.html", context)

@login_required
def checkout_info_view(request, *args, **kwargs):
    """
    Renders checkout info page with navbar and footer removed
    """
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_info"
    }
    return render(request, "checkout1_info.html", context)

@login_required
def checkout_shipping_view(request, *args, **kwargs):
    """
    Renders checkout shipping page with navbar and footer removed
    """
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_shipping"
    }
    return render(request, "checkout2_shipping.html", context)

@login_required
def checkout_payment_view(request, *args, **kwargs):
    """
    Renders checkout payment page with navbar and footer removed
    """
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_payment"
    }
    return render(request, "checkout3_payment.html", context)

@login_required
def checkout_confirm_view(request, *args, **kwargs):
    """
    Renders payment conformation page with navbar and footer removed
    """
    context = {
        "footer": False,
        "navbar": False,
        "active_pg": "checkout_confirm"
    }
    return render(request, "checkout4_confirm.html", context)
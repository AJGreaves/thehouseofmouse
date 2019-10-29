import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
# from django.contrib.auth.models import User
from products.models import Product
from .forms import OrderItemForm

# Create your views here.
@login_required
def cart_view(request, *args, **kwargs):
    """
    render shopping cart page, remove footer from this page
    to fit conventions of other eCommerce sites
    """

    cart = request.session.get('cart')
    cart_items = []

    for item in cart['orderItems']:
        _id = item['listingId']
        product = get_object_or_404(Product, id=_id)
        stock_arr = [x for x in range(product.num_in_stock)]
        cart_items.append({'product': product, 'quantity': item['quantity'], 'stock_arr': stock_arr})
    print(cart)
    print(cart_items)

    initial_data = []
    i = 1
    for item in cart['orderItems']:
        initial_data.append({'name': i, 'quantity': item['quantity']})

    OrderItemFormSet = formset_factory(OrderItemForm, extra=0)
    form = OrderItemFormSet(initial=initial_data)

    context = {
        "cart_items" : cart_items,
        'formset' : form,
        "footer": False
    }

    if request.method == 'POST':
        # Fetch request
        post_request = json.loads(request.body)
        input_id = post_request['idChangedInput']
        input_id = ''.join(i for i in input_id if i.isdigit())
        max_num = cart_items[int(input_id)]['product'].num_in_stock
        request.session['cart']['orderItems'][int(input_id)]['quantity'] = post_request['value']
        request.session.modified = True
        
        response = {
            'max_num': max_num,
            'title': cart_items[int(input_id)]['product'].title,
        }
        return JsonResponse(response)


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
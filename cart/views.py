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

        if int(cart['orderItems'][int(input_id)]['quantity']) <= max_num:
            cart['orderItems'][int(input_id)]['quantity'] = post_request['value']
        else:
            cart['orderItems'][int(input_id)]['quantity'] = max_num

        cart_total_price = 0
        cart_total_quantity = 0
        for item in cart['orderItems']:
            product = get_object_or_404(Product, id=item['listingId'])
            item_price = int(product.price)
            cart_total_quantity = cart_total_quantity + int(item['quantity'])
            cart_total_price = cart_total_price + (item_price * int(item['quantity']))
        
        cart['total'] = cart_total_price
        cart['count'] = cart_total_quantity

        request.session['cart'] = cart

        response = {
            'max_num': max_num,
            'title': cart_items[int(input_id)]['product'].title,
            'total': request.session['cart']['total'],
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
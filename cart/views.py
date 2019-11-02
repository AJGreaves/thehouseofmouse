import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from products.models import Product
from .forms import OrderItemForm
from .models import ShippingDestination, Order, OrderItem

# Create your views here.
@login_required
def cart_view(request, *args, **kwargs):
    """
    render shopping cart page, remove footer from this page
    to fit conventions of other eCommerce sites
    """
    if request.session.get('cart'):
        cart = request.session.get('cart')
        cart_items = []
        print(cart)
        for item in cart['orderItems']:
            _id = item['listingId']
            product = get_object_or_404(Product, id=_id)
            stock_arr = [x for x in range(product.num_in_stock)]
            cart_items.append({'product': product, 'quantity': item['quantity'], 'stock_arr': stock_arr})

        initial_data = []
        i = 1
        for item in cart['orderItems']:
            initial_data.append({'quantity': item['quantity']})

        OrderItemFormSet = formset_factory(OrderItemForm, extra=0)
        form = OrderItemFormSet(initial=initial_data)

        context = {
            "cart_items" : cart_items,
            'formset' : form,
            "footer": False
        }

        if request.method == 'POST':
            
            if request.headers['Content-Type'] == 'application/json':
                # FETCH REQUESTS
                post_request = json.loads(request.body)

                # if change to quantities in cart
                if post_request.get('idChangedInput'):
                    
                    # get item from cart items that was changed by user
                    input_id = post_request['idChangedInput']
                    input_id = ''.join(i for i in input_id if i.isdigit())

                    # get number in stock from database
                    listing_id = cart['orderItems'][int(input_id)]['listingId']
                    product = get_object_or_404(Product, id=listing_id)
                    max_num = product.num_in_stock

                    # get quantity user requested
                    value = int(post_request['value'])

                    # set quantity value by comparing number requested with maximum number in stock
                    quantity = value if value <= max_num else int(max_num)

                    cart['orderItems'][int(input_id)]['quantity'] = quantity

                    cart_total_price = set_new_cart_totals(request, cart)

                    response = {
                        'max_num': max_num,
                        'title': cart_items[int(input_id)]['product'].title,
                        'total': int(cart_total_price),
                    }

                # if user deleted item from cart
                if post_request.get('orderItemId'):

                    id_to_delete = post_request['orderItemId']
                    id_to_delete = int(id_to_delete) - 1

                    # set quantity of item to 0, but do not actually delete entry from session.
                    # I did this to save from changing the indexes of other items in the
                    # session orderItems list.
                    cart['orderItems'][id_to_delete]['quantity'] = 0
                    
                    cart_total_price = set_new_cart_totals(request, cart)

                    # If cart completely empty, delete entire cart data in storage
                    if int(cart_total_price) == 0:
                        del request.session['cart']
                    
                    response = {
                        'total': int(cart_total_price),
                    }

                return JsonResponse(response)

            else:
                # CHECKOUT REQUEST

                # get unpaid order for this user if it already exists
                order = Order.objects.filter(customer=request.user, paid=False).first()
                checkout_cart = request.session['cart']

                # if new order create instance of order
                if not order:
                    order = Order.objects.create(customer=request.user)
                
                # if unpaid order exists in database already:
                else:
                    # get items in session storage cart
                    session_cart = checkout_cart['orderItems']

                    # get items currently in Order
                    items_in_order = OrderItem.objects.filter(order=order)

                    # delete all orders in the list
                    # fixes doubled up items appearing in database due to nested loop I 
                    # was trying to use to compare entries.
                    for orderitem in items_in_order:
                        orderitem.delete()

                    # loop through all cart items and create new instances of OrderItem for them
                    for item in session_cart:
                        _id = int(item['listingId'])
                        quantity = int(item['quantity'])

                        # filter out items in session storage that have had their quantities reduced to 0
                        if quantity > 0:
                            product = Product.objects.filter(id=_id).first()
                            order_item = OrderItem(order=order, product=product, quantity=quantity)
                            order_item.save()
                    
                return redirect('info')
    else:
        context = {
            'nothing_in_cart': True,
            'footer': False
        }
    return render(request, "cart.html", context)

def set_new_cart_totals(request, cart):
    """
    loops through cart contents to get new quantity and total,
    then sets the session variables to reflect them
    """
    cart_total_price = 0
    cart_total_quantity = 0
    for item in cart['orderItems']:
        product = get_object_or_404(Product, id=item['listingId'])
        item_price = int(product.price)
        cart_total_quantity = cart_total_quantity + int(item['quantity'])
        cart_total_price = cart_total_price + (item_price * int(item['quantity']))
    
    cart['total'] = int(cart_total_price)
    cart['count'] = int(cart_total_quantity)

    # reset cart in session
    request.session['cart'] = cart

    return cart_total_price

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
import json
import env
import stripe
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory
from products.models import Product
from .forms import OrderItemForm, NewOrderForm
from .models import Order, OrderItem, ShippingDestination
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
@login_required
def cart_view(request, *args, **kwargs):
    """
    render shopping cart page, remove footer from this page
    to fit conventions of other eCommerce sites
    """
    if request.session.get('cart'):
        cart = request.session.get('cart')
        context = get_cart_page_context(cart)

        if request.method == 'POST':
            
            if request.headers['Content-Type'] == 'application/json':
                # FETCH REQUESTS
                post_request = json.loads(request.body)

                # if change to quantities in cart
                if post_request.get('idChangedInput'):
                    response = process_changed_input_request(request, post_request, cart)

                # if user deleted item from cart
                if post_request.get('orderItemId'):
                    response = process_delete_request(request, post_request, cart)

                return JsonResponse(response)

            else:
                # CHECKOUT REQUEST

                # get unpaid order for this user if it already exists
                order = Order.objects.filter(customer=request.user, paid=False).first()
                checkout_cart = request.session['cart']

                # if new order create instance of order
                if not order:
                    order = Order.objects.create(customer=request.user)
                
                create_order_items(order, checkout_cart)
                    
                return redirect('info')

    else:
        context = {
            'nothing_in_cart': True,
            'footer': False
        }
    return render(request, "cart.html", context)

@login_required
def checkout_info_view(request, *args, **kwargs):
    """
    Renders checkout info page with navbar and footer removed
    """

    # If user trying to navigate to this page with nothing in their cart, redirect them to cart page
    # that shows message "You have nothing in your cart yet."
    if not request.session.get('cart'):
        return redirect('cart')

    else:
        cart = request.session.get('cart')
        context = get_cart_page_context(cart)

        # get unpaid order for this user
        order = Order.objects.filter(customer=request.user, paid=False).first()

        if request.method == 'POST':
            
            order_form = NewOrderForm(request.POST)

            if order_form.is_valid():
                # Extract form data and insert into order instance.
                order.full_name = request.POST.get('full_name')
                order.address_line_1 = request.POST.get('address_line_1')
                order.address_line_2 = request.POST.get('address_line_2')
                order.town_or_city = request.POST.get('town_or_city')
                order.county = request.POST.get('county')
                order.postcode = request.POST.get('postcode').upper()
                order.country = ShippingDestination.objects.get(id=request.POST.get('country'))
                order.save()

            else:
                return HttpResponse(order_form.errors)

            return redirect('shipping')

    # Get any data for shipping info already in order:
    initial_data = {
        'full_name': order.full_name,
        'address_line_1': order.address_line_1,
        'address_line_2': order.address_line_2,
        'town_or_city': order.town_or_city,
        'county': order.county,
        'postcode': order.postcode,
        'country': order.country,
    }

    shipping_info_form = NewOrderForm(initial=initial_data)

    new_context = {
        **context,
        **{
            "active_pg": "checkout_info",
            "shipping_info_form" : shipping_info_form,
            "navbar": False
        }
    }

    return render(request, "checkout1_info.html", new_context)

@login_required
def checkout_shipping_view(request, *args, **kwargs):
    """
    Renders checkout shipping page with navbar and footer removed
    """
    if not request.session.get('cart'):
        return redirect('cart')

    else:
        cart = request.session.get('cart')
        context = get_cart_page_context(cart)

        # get unpaid order for this user
        order = Order.objects.filter(customer=request.user, paid=False).first()

        if request.method == 'POST':
            return redirect('payment')

        new_context = {
            **context,
            **{
                "active_pg": "checkout_shipping",
                "navbar": False,
                "order": order,
                "user": request.user,
                'publishable': settings.STRIPE_PUBLISHABLE
            }
        }
        return render(request, "checkout2_shipping.html", new_context)

@login_required
def checkout_payment_view(request, *args, **kwargs):
    """
    Renders checkout payment page with navbar and footer removed
    """
    if not request.session.get('cart'):
        return redirect('cart')
    
    else:
        cart = request.session.get('cart')
        context = get_cart_page_context(cart)

        # get unpaid order for this user
        order = Order.objects.filter(customer=request.user, paid=False).first()

        if request.method == 'POST':

            total = 0
            for item in cart['orderItems']:
                product = get_object_or_404(Product, pk=item['listingId'])
                total += item['quantity'] * product.price

            total += order.country.shipping_price
            print(total)

            # when stripe successful update order paid
            # return redirect('confirm')
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'T-shirt',
                'description': 'Comfortable cotton t-shirt',
                'images': ['https://example.com/t-shirt.png'],
                'amount': 500,
                'currency': 'eur',
                'quantity': 1,
            }],
            success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://example.com/cancel',
        )

        new_context = {
            **context,
            **{
                "active_pg": "checkout_payment",
                "navbar": False,
                "order": order,
                "user": request.user
            }
        }
        return render(request, "checkout3_payment.html", new_context)

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



# HELPER FUNCTIONS

def create_order_items(order, checkout_cart):
    """
    Creates new OrderItems for Order from cart stored in session. 
    If an Order for user already exists, deletes all related OrderItems 
    from it first and then rebuilds from session cart. 
    """
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
    return

def process_delete_request(request, post_request, cart):
    """
    Processes request from user to delete item from their cart. 
    Reduces deleted item quantity to 0 and returns response to be sent to js fetch.
    """
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
    return response

def process_changed_input_request(request, post_request, cart):
    """
    Processes request from user to change cart item quantity. 
    Returns response to be sent to js fetch.
    """
    print(cart)
    cart_items = get_cart_items(cart)
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
    return response

def get_cart_page_context(cart):
    """ gets context to display contents of cart """
    cart_items = get_cart_items(cart)
    initial_data = get_initial_data(cart)
    OrderItemFormSet = formset_factory(OrderItemForm, extra=0)
    form = OrderItemFormSet(initial=initial_data)

    context = {
        "cart_items" : cart_items,
        'formset' : form,
        "footer": False
    }

    return context

def get_initial_data(cart):
    """ Creates initial data for quantity fields in OrderForm """
    data = []
    for item in cart['orderItems']:
        data.append({'quantity': item['quantity']})
    return data

def get_cart_items(cart):
    """ Gets data needed for rendering cart items in html """
    cart_items = []
    for item in cart['orderItems']:
        _id = item['listingId']
        product = get_object_or_404(Product, id=_id)
        stock_arr = [x for x in range(product.num_in_stock)]
        cart_items.append({'product': product, 'quantity': item['quantity'], 'stock_arr': stock_arr})
    return cart_items

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
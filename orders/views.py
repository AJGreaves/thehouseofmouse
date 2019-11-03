from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from cart.models import Order

# Create your views here.
@staff_member_required
def orders_view(request, *args, **kwargs):
    """
    Render order view for staff to view orders
    """
    orders = Order.objects.filter(paid=True)

    # context to get order items too.
    
    context = {
        "orders": orders
    }

    return render(request, 'orders.html', context)
from django import forms
from .models import Order, OrderItem

class OrderItemForm(forms.ModelForm):
    """ form for cart view, so the user can update quantity of product they want to order. """
    quantity = forms.IntegerField(
        min_value=0,
        max_value=10
    )
    class Meta:
        model = OrderItem
        fields = [
            'quantity'
        ]

class NewOrderForm(forms.ModelForm):

    """ Form to collect shipping information for order on checkout_info page """
    class Meta:
        model = Order
        fields = [
            'full_name',
            'address_line_1',
            'address_line_2',
            'town_or_city',
            'county',
            'postcode',
            'country',
        ]

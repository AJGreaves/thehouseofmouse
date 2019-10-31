from django import forms
from .models import Order, OrderItem

class OrderItemForm(forms.ModelForm):

    quantity = forms.IntegerField(
        label='',
        min_value='0',
        max_value=10
    )
    class Meta:
        model = OrderItem
        fields = [
            'quantity'
        ]

class NewOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'full_name',
            'address_line_1',
            'address_line_2',
            'town_or_city',
            'county',
            # 'country'
        ]
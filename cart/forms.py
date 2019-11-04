from django import forms
from .models import Order, OrderItem

class OrderItemForm(forms.ModelForm):

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

class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]

    credit_cart_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label="Security code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
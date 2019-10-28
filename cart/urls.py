from django.urls import path
from .views import (
    cart_view,
    checkout_info_view,
    checkout_shipping_view,
    checkout_payment_view,
    checkout_confirm_view
)

urlpatterns = [
    path('', cart_view, name="cart"),
    path('checkout/info/', checkout_info_view, name="info"),
    path('checkout/shipping/', checkout_shipping_view, name="shipping"),
    path('checkout/payment/', checkout_payment_view, name="payment"),
    path('checkout/confirm/', checkout_confirm_view, name="confirm")
]